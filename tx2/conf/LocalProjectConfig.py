

# SYSTEM PERMISSIONS
SYSTEM_PERMISSION_INSERT = 'SYS_PER_INSERT'
SYSTEM_PERMISSION_UPDATE = 'SYS_PER_UPDATE'
SYSTEM_PERMISSION_DELETE = 'SYS_PER_DELETE'
SYSTEM_PERMISSION_EMAIL_AU = 'SYS_PER_USER_AU_EMAIL'
SYSTEM_PERMISSION = (SYSTEM_PERMISSION_INSERT,SYSTEM_PERMISSION_UPDATE,SYSTEM_PERMISSION_DELETE,SYSTEM_PERMISSION_EMAIL_AU)

# SYSTEM STATES
SYSTEM_STATE_ACTIVE = 'SYS_STATE_ACTIVE'
SYSTEM_STATE_DELETED = 'SYS_STATE_DELETED'
SYSTEM_STATE_USER_REGISTER = 'SYS_STATE_USER_CREATED'
SYSTEM_STATE_USER_EMAIL_AU = 'SYS_STATE_USER_AU_EMAIL'
SYSTEM_STATE = (SYSTEM_STATE_ACTIVE,SYSTEM_STATE_DELETED,SYSTEM_STATE_USER_REGISTER,SYSTEM_STATE_USER_EMAIL_AU)

#DEFAULT USER SYSTEM

#ENTITY
SYSTEM_ENTITY = 'SystemInit'
CACHE_KEY_SYSTEM_ENTITY = 'CACHE_KEY_SYSTEM_ENTITY'

# GROUP TYPE
SYSTEM_GROUPTYPE = 'SystemInit'
SYSTEM_GROUP = 'SystemInit'

SYSTEM_INIT_USER = 'SystemInit1@init.com'
SYSTEM_LOGINTYPE = 'SystemInit'

# INITIALISATION USERNAME AND PASSWORD
SYSTEM_INITIALISE_USERNAME = 'tx2'
SYSTEM_INITIALISE_PASSWORD = 'tx2'

# LOGGER NAME
SYSTEM_INITIALISE_LOGGER = 'SYSTEM_INITIALISE_LOGGER'

#MISC
SYSTEM_INITIALISE_SESSION_NAME = 'AdminInitLoginSession'

#DAEMONS
SYSTEM_CREATEUSERDAEMON_GROUP = 'Daemon_CreateUserGroup'
SYSTEM_DAEMON_CREATE_USER = 'Daemon_CreateUser@system.com'
CACHE_KEY_SYSTEM_DAEMON_CREATE_USER = 'CACHE_KEY_SYSTEM_DAEMON_CREATE_USER'
SYSTEM_DAEMON_CREATE_USER_GROUP = 'Daemon_RegisteredUsers'
CACHE_KEY_NEW_USERS_GROUP = 'CACHE_KEY_NEW_USERS_GROUP'
SYSTEM_DAEMON_USERAU_USER_GROUP = 'Daemon_UserAuUsers'
CACHE_KEY_SYSTEM_DAEMON_USERAU_USER_GROUP = 'CACHE_KEY_SYSTEM_DAEMON_USERAU_USER_GROUP'


# SYSTEM WIDE CACHE KEYS
CACHE_CONTENTTYPES_LIST = 'CACHE_KEY_CONTENT_TYPES'

