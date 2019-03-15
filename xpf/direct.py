"""
This is an auto-generated wrapper to make it easier to access the standard
perforce functionalities. 

All commands called through here are failsafe. All the calls are correctly
marshalled for you.

You can pass the following special keywords to any of these calls:

    :timeout: This is the maximum amount of time you're willing to
        allow the call to take. If the time exceeds this the call will be
        abandoned.
        The default of this is 1 second, but can be altered using
        xpf.variables.set_timeout(value)
    
    :return_type: If a timeout occurs this is the return type that will
        be given back. Typically this is not required as all functions are
        decorated with a failsafe which defines the return type. But this allows
        that to be overriden.
        
    :form: If you need to pass in a form to the call (where p4 would
        typically open a text window, you can pass a dictionary to this 
        argument and that will be resolved as the form input.
    
    :marshal: If True the return values will be marshaled to python
        dictionaries. The default of this argument is True.
        
    :port: This is the port (server address:port to be used during
        the call. By default this is taken from the `P4 set` call which 
        happens during the first call. 
        You can also globally override this using xpf.variables.set_port(value)
        
    :client: By default the client is taken from an inital `p4 set` call
        and passed through. But you can optionally pass it a bespoke client.
        If you're working in a multi-workspace environment its advisable to 
        utilise p4config as that mechanism allows this to be automatically
        resolved within perforce.
        
"""
from . import failsafe
from . import connection


# ------------------------------------------------------------------------------
@failsafe.return_list
def run(*args, **kwargs):
    return connection.safe_run(*args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def add(*args, **kwargs):
    return run('add',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def admin(*args, **kwargs):
    return run('admin',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def aliases(*args, **kwargs):
    return run('aliases',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def annotate(*args, **kwargs):
    return run('annotate',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def archive(*args, **kwargs):
    return run('archive',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def attribute(*args, **kwargs):
    return run('attribute',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def bgtask(*args, **kwargs):
    return run('bgtask',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def branch(*args, **kwargs):
    return run('branch',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def branches(*args, **kwargs):
    return run('branches',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def cachepurge(*args, **kwargs):
    return run('cachepurge',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def change(*args, **kwargs):
    return run('change',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def changelist(*args, **kwargs):
    return run('changelist',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def changelists(*args, **kwargs):
    return run('changelists',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def changes(*args, **kwargs):
    return run('changes',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def clean(*args, **kwargs):
    return run('clean',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def client(*args, **kwargs):
    return run('client',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def clients(*args, **kwargs):
    return run('clients',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def clone(*args, **kwargs):
    return run('clone',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def configure(*args, **kwargs):
    return run('configure',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def copy(*args, **kwargs):
    return run('copy',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def counter(*args, **kwargs):
    return run('counter',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def counters(*args, **kwargs):
    return run('counters',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def cstat(*args, **kwargs):
    return run('cstat',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def dbschema(*args, **kwargs):
    return run('dbschema',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def dbstat(*args, **kwargs):
    return run('dbstat',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def dbverify(*args, **kwargs):
    return run('dbverify',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def delete(*args, **kwargs):
    return run('delete',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def depot(*args, **kwargs):
    return run('depot',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def depots(*args, **kwargs):
    return run('depots',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def describe(*args, **kwargs):
    return run('describe',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def diff(*args, **kwargs):
    return run('diff',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def diff2(*args, **kwargs):
    return run('diff2',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def dirs(*args, **kwargs):
    return run('dirs',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def diskspace(*args, **kwargs):
    return run('diskspace',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def edit(*args, **kwargs):
    return run('edit',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def export(*args, **kwargs):
    return run('export',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def failover(*args, **kwargs):
    return run('failover',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def fetch(*args, **kwargs):
    return run('fetch',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def filelog(*args, **kwargs):
    return run('filelog',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def files(*args, **kwargs):
    return run('files',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def fix(*args, **kwargs):
    return run('fix',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def fixes(*args, **kwargs):
    return run('fixes',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def flush(*args, **kwargs):
    return run('flush',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def fstat(*args, **kwargs):
    return run('fstat',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def grep(*args, **kwargs):
    return run('grep',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def group(*args, **kwargs):
    return run('group',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def groups(*args, **kwargs):
    return run('groups',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def have(*args, **kwargs):
    return run('have',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def help_(*args, **kwargs):
    return run('help',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def ignores(*args, **kwargs):
    return run('ignores',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def info(*args, **kwargs):
    return run('info',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def init(*args, **kwargs):
    return run('init',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def integrate(*args, **kwargs):
    return run('integrate',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def integrated(*args, **kwargs):
    return run('integrated',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def interchanges(*args, **kwargs):
    return run('interchanges',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def istat(*args, **kwargs):
    return run('istat',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def job(*args, **kwargs):
    return run('job',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def jobs(*args, **kwargs):
    return run('jobs',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def jobspec(*args, **kwargs):
    return run('jobspec',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def journalcopy(*args, **kwargs):
    return run('journalcopy',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def journaldbchecksums(*args, **kwargs):
    return run('journaldbchecksums',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def journals(*args, **kwargs):
    return run('journals',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def key(*args, **kwargs):
    return run('key',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def keys(*args, **kwargs):
    return run('keys',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def label(*args, **kwargs):
    return run('label',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def labels(*args, **kwargs):
    return run('labels',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def labelsync(*args, **kwargs):
    return run('labelsync',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def ldap(*args, **kwargs):
    return run('ldap',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def ldaps(*args, **kwargs):
    return run('ldaps',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def ldapsync(*args, **kwargs):
    return run('ldapsync',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def license_(*args, **kwargs):
    return run('license',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def list_(*args, **kwargs):
    return run('list',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def lock(*args, **kwargs):
    return run('lock',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def lockstat(*args, **kwargs):
    return run('lockstat',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def logappend(*args, **kwargs):
    return run('logappend',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def logger(*args, **kwargs):
    return run('logger',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def login(*args, **kwargs):
    return run('login',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def login2(*args, **kwargs):
    return run('login2',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def logout(*args, **kwargs):
    return run('logout',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def logparse(*args, **kwargs):
    return run('logparse',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def logrotate(*args, **kwargs):
    return run('logrotate',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def logschema(*args, **kwargs):
    return run('logschema',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def logstat(*args, **kwargs):
    return run('logstat',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def logtail(*args, **kwargs):
    return run('logtail',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def merge(*args, **kwargs):
    return run('merge',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def monitor(*args, **kwargs):
    return run('monitor',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def move(*args, **kwargs):
    return run('move',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def obliterate(*args, **kwargs):
    return run('obliterate',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def opened(*args, **kwargs):
    return run('opened',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def passwd(*args, **kwargs):
    return run('passwd',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def ping(*args, **kwargs):
    return run('ping',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def populate(*args, **kwargs):
    return run('populate',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def print_(*args, **kwargs):
    return run('print',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def property_(*args, **kwargs):
    return run('property',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def protect(*args, **kwargs):
    return run('protect',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def protects(*args, **kwargs):
    return run('protects',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def proxy(*args, **kwargs):
    return run('proxy',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def prune(*args, **kwargs):
    return run('prune',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def pull(*args, **kwargs):
    return run('pull',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def push(*args, **kwargs):
    return run('push',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def reconcile(*args, **kwargs):
    return run('reconcile',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def reload_(*args, **kwargs):
    return run('reload',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def remote(*args, **kwargs):
    return run('remote',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def remotes(*args, **kwargs):
    return run('remotes',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def rename(*args, **kwargs):
    return run('rename',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def renameuser(*args, **kwargs):
    return run('renameuser',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def reopen(*args, **kwargs):
    return run('reopen',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def replicate(*args, **kwargs):
    return run('replicate',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def reshelve(*args, **kwargs):
    return run('reshelve',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def resolve(*args, **kwargs):
    return run('resolve',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def resolved(*args, **kwargs):
    return run('resolved',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def restore(*args, **kwargs):
    return run('restore',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def resubmit(*args, **kwargs):
    return run('resubmit',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def revert(*args, **kwargs):
    return run('revert',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def review(*args, **kwargs):
    return run('review',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def reviews(*args, **kwargs):
    return run('reviews',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def server(*args, **kwargs):
    return run('server',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def serverid(*args, **kwargs):
    return run('serverid',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def servers(*args, **kwargs):
    return run('servers',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def set_(*args, **kwargs):
    return run('set',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def shelve(*args, **kwargs):
    return run('shelve',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def sizes(*args, **kwargs):
    return run('sizes',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def status(*args, **kwargs):
    return run('status',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def stream(*args, **kwargs):
    return run('stream',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def streams(*args, **kwargs):
    return run('streams',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def submit(*args, **kwargs):
    return run('submit',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def switch(*args, **kwargs):
    return run('switch',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def sync(*args, **kwargs):
    return run('sync',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def tag(*args, **kwargs):
    return run('tag',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def tickets(*args, **kwargs):
    return run('tickets',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def triggers(*args, **kwargs):
    return run('triggers',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def trust(*args, **kwargs):
    return run('trust',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def typemap(*args, **kwargs):
    return run('typemap',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def undo(*args, **kwargs):
    return run('undo',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def unload(*args, **kwargs):
    return run('unload',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def unlock(*args, **kwargs):
    return run('unlock',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def unshelve(*args, **kwargs):
    return run('unshelve',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def unsubmit(*args, **kwargs):
    return run('unsubmit',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def unzip(*args, **kwargs):
    return run('unzip',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def update(*args, **kwargs):
    return run('update',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def user(*args, **kwargs):
    return run('user',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def users(*args, **kwargs):
    return run('users',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def verify(*args, **kwargs):
    return run('verify',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def where(*args, **kwargs):
    return run('where',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def workspace(*args, **kwargs):
    return run('workspace',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def workspaces(*args, **kwargs):
    return run('workspaces',  *args, **kwargs)


# ------------------------------------------------------------------------------
@failsafe.return_list
def zip_(*args, **kwargs):
    return run('zip',  *args, **kwargs)
