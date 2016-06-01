PROJECT="${PWD##*/}"
DOCKER_MACHINE="docker-machine"
DOCKER_MACHINE_STATUS="${DOCKER_MACHINE} status "${PROJECT}" 2>&1"
DOCKER_MACHINE_CREATE="${DOCKER_MACHINE} create --driver virtualbox "${PROJECT}""
DOCKER_MACHINE_NOT_FOUND_STATUS="Host does not exist"
DOCKER_MACHINE_PREPARE_MESSAGE="Preparing environment: ${PROJECT}"
DOCKER_MACHINE_CREATE_MESSAGE="Creating docker machine (${PROJECT}) since it was not found."
DOCKER_MACHINE_EXISTS_MESSAGE="The docker machine (${PROJECT}) already exists."
DOCKER_MACHINE_ENV="${DOCKER_MACHINE} env ${PROJECT}"
DOCKER_MACHINE_IP="${DOCKER_MACHINE} ip ${PROJECT}"
DOCKER_MACHINE_START="${DOCKER_MACHINE} start ${PROJECT}"

DOCKER_COMPOSE="docker-compose"
DOCKER_COMPOSE_UP="${DOCKER_COMPOSE} up"

eval ${DOCKER_MACHINE_STATUS}

#eval ${DOCKER_MACHINE_CREATE}
#eval ${DOCKER_MACHINE_START}
#eval $(docker-machine env ${PROJECT})
#eval ${DOCKER_MACHINE_IP}
#eval ${DOCKER_COMPOSE_UP}
