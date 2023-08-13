import paramiko
import re
import os
"""
#Одиночная команда

import paramiko
key_file = "path\\to]\private\\key"
# Создаем объект SSHClient
ssh = paramiko.SSHClient()

# Устанавливаем политику подключения
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Подключаемся к удаленной машине
ssh.connect('ip', username='username', key_filename=key_file)

stdin, stdout, stderr = ssh.exec_command('cd distr; ls')
print(stdout.read().decode())
"""



class SFTPClient():
    """Объект отправки / получения файлов / каталогов на удаленную машину через SSH

    .. code-block:: python

        from pyOpenRPA.Utils import SSH
        RemoteSFTP=SSH.SFTPClient(host_str="localhost", port_int=22, user_str="root", key_path_str="path\\to\\file)
        # Отправляем файлы (папку) на удаленную машину
        RemoteSFTP.mkdir(DEPLOY_FOLDER_REMOTE_PATH_STR)
        RemoteSFTP.put_dir(DEPLOY_LOCAL_PATH_STR, DEPLOY_REMOTE_PATH_STR)
        RemoteSFTP.put_dir(DEPLOY_FOLDER_LOCAL_PATH_STR, DEPLOY_FOLDER_REMOTE_PATH_STR)
        # Закрываем соединение
        RemoteSFTP.close()


    :param paramiko: _description_
    :type paramiko: _type_
    """
    sftp = None
    transport = None
    def __init__(self, host_str="localhost", port_int=22, user_str="root", key_path_str=None):
        self.transport = paramiko.Transport((host_str, port_int))
        pkey = paramiko.RSAKey.from_private_key_file(key_path_str)#, password='12345')
        # Подключаемся к удаленной машине
        self.transport.connect(username=user_str, pkey=pkey)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def put(self, source, target):
        self.put(source, target)

    def put_dir(self, source, target):
        ''' Uploads the contents of the source directory to the target path. The
            target directory needs to exists. All subdirectories in source are
            created under target.
        '''
        for item in os.listdir(source):
            if os.path.isfile(os.path.join(source, item)):
                self.sftp.put(os.path.join(source, item), '%s/%s' % (target, item))
            else:
                self.mkdir('%s/%s' % (target, item), ignore_existing=True)
                self.put_dir(os.path.join(source, item), '%s/%s' % (target, item))
    def mkdir(self, path, mode=511, ignore_existing=False):
        '''Augments mkdir by adding an option to not fail if the folder exists'''
        try:
            self.sftp.mkdir(path, mode)
        except IOError:
            if ignore_existing:
                pass
            else:
                raise
    def close(self):
        self.sftp.close()
        self.transport.close()

class Shell:
    """Объект терминала, подключенный по SSH. Хранит состояние предыдущих команд (например cd)

    .. code-block:: python

        from pyOpenRPA.Utils import SSH
        RemoteShell=SSH.Shell(host_str="localhost", port_int=22, user_str="root", key_path_str="path\\to\\file)
        print(RemoteShell.exec_command('cd folder_name'))
        print(RemoteShell.exec_command('ls'))
        
    """
    def __init__(self, host_str="localhost", port_int=22, user_str="root", key_path_str=None):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host_str, username=user_str, key_filename=key_path_str)
        channel = self.ssh.invoke_shell()
        self.stdin = channel.makefile('wb')
        self.stdout = channel.makefile('r')
    def __del__(self):
        self.stdin.close()
        self.stdout.close()
        self.ssh.close()
    def exec_command(self, cmd):
        """
        :param cmd: the command to be executed on the remote computer
        :examples:  exec_command('ls')
                    exec_command('finger')
                    exec_command('cd folder_name')
        :return: [<channel>, [stdout lines], [stderr lines]]
        """
        cmd = cmd.strip('\n')
        self.stdin.write(cmd + '\n')
        finish = 'end of stdOUT buffer. finished with exit status'
        echo_cmd = 'echo {} $?'.format(finish)
        self.stdin.write(echo_cmd + '\n')
        shin = self.stdin
        self.stdin.flush()
        shout = []
        sherr = []
        exit_status = 0
        for line in self.stdout:
            if str(line).startswith(cmd) or str(line).startswith(echo_cmd):
                # up for now filled with shell junk from stdin
                shout = []
            elif str(line).startswith(finish):
                # our finish command ends with the exit status
                exit_status = int(str(line).rsplit(maxsplit=1)[1])
                if exit_status:
                    # stderr is combined with stdout.
                    # thus, swap sherr with shout in a case of failure.
                    sherr = shout
                    shout = []
                break
            else:
                # get rid of 'coloring and formatting' special characters
                shout.append(re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]').sub('', line).
                             replace('\b', '').replace('\r', ''))
        # first and last lines of shout/sherr contain a prompt
        if shout and echo_cmd in shout[-1]:
            shout.pop()
        if shout and cmd in shout[0]:
            shout.pop(0)
        if sherr and echo_cmd in sherr[-1]:
            sherr.pop()
        if sherr and cmd in sherr[0]:
            sherr.pop(0)
        return shin, shout, sherr