import time
from distutils.core import setup

setup(
  name='buckets',
  packages=['buckets'],
  scripts=['bin/buckets-gen-cert'],
  version=time.strftime('%Y%m%d'),
  description='Strongly consistent KV store and Log - '
              'with GET/PUT/APPEND operations over HTTPS.',
  long_description='Uses Paxos for replication, SQLite for paxos metadata and '
                   'filesystem for data. Leaderless and highly available.',
  author='Bhupendra Singh',
  author_email='bhsingh@gmail.com',
  url='https://github.com/magicray/buckets',
  keywords=['paxos', 'kv', 'key', 'value', 'sqlite', 'consistent']
)
