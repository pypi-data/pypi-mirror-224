import json

import qiskit
from concurrent import futures
import dateutil.parser
from typing import Dict, Optional, Tuple, Any, List, Callable, Union

from qiskit.compiler import assemble
from qiskit.providers import  BackendV1
from qiskit.providers.provider import ProviderV1
from qiskit.providers.job import JobV1 as Job
from qiskit.providers.models import BackendConfiguration
 
from qiskit_aer import AerSimulator
from qiskit.providers.options import Options
import mysql.connector as mysql
import os 
from dotenv import load_dotenv
import os
import requests
import time 
import random
import string 


load_dotenv()

db = mysql.connect(user=os.environ.get('DB_USERNAME'), 
                     password=os.environ.get('DB_PASSWORD'),
                     host=os.environ.get('DB_HOST'),
                     database=os.environ.get('DB_TYPE'))

class QuantierJob(Job):
    def __init__(self, backend, qobj, **kwargs):
        self._backend=backend
        self.job_dict = self.assemble_and_prepare_job(qobj, **kwargs)
        self.job_json = json.dumps(self.job_dict)
        
        #Generate Job ID
        self.job_id = self.generate_string()
        
        super().__init__(backend, job_id=self.job_id) # Use actual job_id as per your requirements
    
    def generate_string(self):
        backend_name = self._backend.name()  
        timestamp = int(time.time() * 1000) 
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Random string of length 8
        return f"jobId-{backend_name}-{timestamp}-{random_string}"
    
    def assemble_and_prepare_job(self, qobj, **kwargs):
        job = assemble(qobj).to_dict()
        job['header']['backend_name'] = self._backend.name()
        job['header']['backend_version'] = self._backend.configuration().backend_version
        job['config']['shots'] = kwargs.get('shots', 5)
        job['config']['memory'] = kwargs.get('memory', "True")
        job['config']['init_qubits'] = kwargs.get('init_qubits', "True")
        job['config']['parameter_binds'] = kwargs.get('parameter_binds', [])
        return job

    # Following are the mandatory methods to be implemented for a Job.
    def result(self, timeout=None):
        #DB Connection
        cursor = db.cursor()
        cursor.execute('''select status from Job where jobid = %s''', [self.job_id])
        status = cursor.fetchone()[0]
        cursor.close()
        db.commit()
        print(status)
        if status == 'COMPLETED':
            cursor = db.cursor()
            cursor.execute('''select result from Result where jobid = %s''', [self.job_id])
            result = cursor.fetchone()[0]
            cursor.close()
            db.commit()
            return result
        else:
          
            print("JOB NOT COMPLETED")
          
    def cancel(self):
        pass  # implement your logic here

    def status(self):
        cursor = db.cursor()
        
        cursor.execute('''select status from Job where jobid = %s''', [self.job_id])
        
        status = cursor.fetchone()[0]

        cursor.close()
        db.commit()
        return status

    def backend(self):
        return self._backend

    def job_id(self):
        return self.job_id  # implement your logic here

    def submit(self):
        pass  # implement your logic here

    def print(self):
        return self.job_json
     
    def job_dict(self):
        return self.job_dict



class QuantierBackend(BackendV1):
    def __init__(self, token):
        configuration = BackendConfiguration(
            backend_name='quantier_backend',
            backend_version='1.0.0',
            n_qubits=32,
            basis_gates=['x', 'y', 'z', 'h', 'cx', 'id'],
            simulator=True,
            local=True,
            conditional=False,
            open_pulse=False,
            memory=True,
            max_shots=1000000,
            max_experiments=1,
            gates=[],
            coupling_map=None
        )
        self._token = token
        self._aer_simulator = AerSimulator()
        super().__init__(configuration=configuration)
    
    def save_job(self, job):
        post_obj = {  
          "job_id": job.job_id,
          "job_json": job.job_json,
          "email":  os.getcwd().split('/')[-1]
        }
        url = os.environ.get('HOST_URL') + '/job/savejob'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + self._token}
        response = requests.post(url, json=post_obj, headers=headers)
        json_response = json.loads(response.content.decode('utf-8'))
        if json_response['status_code'] == 200:
          cursor = db.cursor()
          cursor.execute('''update Job set status = 'JOB CREATED!!' where jobid = (%s)''', [job.job_id])
          
          cursor.close()
        else:
          cursor = db.cursor()
          cursor.execute('''update Job set status = 'JOB CREATION FAILED' where jobid = (%s)''', [job.job_id])
          cursor.close()
        db.commit()
        
    def queue_job(self, job):
        post_obj = {  
          "job_id": job.job_id,
          "job_json": job.job_dict
        }
        
        url = os.environ.get('HOST_URL') + '/job/queuejob'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + self._token}
        
        response = requests.post(url, json=post_obj, headers=headers)
        json_response = json.loads(response.content.decode('utf-8'))
        if json_response['status_code'] == 200:
          cursor = db.cursor()
          cursor.execute('''update Job set status = 'QUEUED' where jobid = (%s)''', [job.job_id])
          cursor.close()
        else:
          cursor = db.cursor()
          cursor.execute('''update Job set status = 'QUEUED REQUEST FAILED' where jobid = (%s)''', [job.job_id])
          cursor.close()
        db.commit()
          
    def run(self, qobj, **kwargs):        
        #Create Job
        print("CREATING JOB")
        job = QuantierJob(self, qobj, **kwargs)
        
        #Save Job
        print("SAVING JOB")
        self.save_job(job)
        
        #Queue Job
        print("QUEUING JOB")
        self.queue_job(job)
        
        #DB Connection
        # cursor = db.cursor()
        
        # #Save Transaction
        # jobid = job.job_id
        # status = job.status
        # email = os.getcwd().split('/')[-1]
        # createdate = time.strftime('%Y-%m-%d %H:%M:%S')
        # qobj_json = job.json_str
                
        # cursor.execute('''insert into transaction 
        #                (jobid, email, createdate, status, qobj_json) values (%s, %s, %s, %s, %s)''',
        #                (jobid, email, createdate, status, qobj_json))
        
        
        
        # #Save Job
        # qobj_id = job.job_dict['qobj_id']
        # header = json.dumps(job.job_dict['header'])
        
        # cursor.execute('''insert into Job 
        #                (jobid, email, qobj_id, status, header, createdate) values (%s, %s, %s, %s, %s, %s)''',
        #                (jobid, email, qobj_id, status, header, createdate))
       
        # cursor.close()
        # db.commit()
        # print("SAVED JOB")
        return (job)
   
    @classmethod
    def _default_options(cls):
        return Options()



class QuantierProvider(ProviderV1):
    def __init__(self, token):
        super().__init__()
        self._backend = QuantierBackend(token)
        self._simulator = AerSimulator()
        self._token = token

    def get_backend(self, name=None, **kwargs):
        if name is None or name.lower() == 'quantier_simulator':
            return self._simulator
        elif name.lower() == 'quantier':
            return self._backend
        else:
            raise qiskit.providers.exceptions.QiskitBackendNotFoundError('Backend not found')

    def backends(self, name=None, **kwargs):
        if name is None:
            return [self._simulator, self._backend]
        if name.lower() == 'quantier':
            return [self._backend]
        if name.lower() == 'quantier_simulator':
            return [self._simulator]
        else:
            return []