import docker


def run_docker_containers(root_dir):
    client = docker.from_env()
    mysql = client.containers.run(
        'mysql:latest',
        name='mysql',
        ports={3306: 3306},
        environment={
            'MYSQL_ROOT_PASSWORD': 'gitea',
            'MYSQL_USER': 'gitea',
            'MYSQL_PASSWORD': 'gitea',
            'MYSQL_DATABASE': 'gitea'},
        detach=True
    )
    volume = client.volumes.create(name='gitea', driver='local')
    gitea = client.containers.run(
        'gitea/gitea:latest',
        name='gitea',
        ports={3000: 3000},
        volumes={
            f'gitea': {'bind': '/data', 'mode': 'rw'},
            f'{root_dir}/app.ini': {'bind': '/data/gitea/conf/app.ini', 'mode': 'rw'},
            '/etc/timezone': {'bind': '/etc/timezone', 'mode': 'rw'},
            '/etc/localtime': {'bind': '/etc/localtime', 'mode': 'rw'},
        },
        environment={
            'GITEA__database__DB_TYPE': 'mysql',
            'GITEA__database__HOST': 'mysql:3306',
            'GITEA__database__NAME': 'gitea',
            'GITEA__database__USER': 'gitea',
            'GITEA__database__PASSWD': 'gitea'
        },
        links={'mysql': None},
        detach=True
    )


def stop_docker_containers():
    client = docker.from_env()
    for container in client.containers.list():
        container.stop()
    client.containers.prune()
