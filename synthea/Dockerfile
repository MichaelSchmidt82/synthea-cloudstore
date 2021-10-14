FROM openjdk:18-slim

#* Install wget
RUN apt-get update \
    && apt-get install -y wget \
    && rm -rf /var/lib/apt/lists/*

#* Build arguements
ARG SYNTHEA_BRANCH="master-branch-latest"
ARG SYNTHEA_FILE="synthea-with-dependencies"

#* Environmental variables
ENV SYNTHEA_FILE=${SYNTHEA_FILE}
ENV SYNTHEA_BRANCH=${SYNTHEA_BRANCH}

ENV NUMBER_OF_RECORDS=100
ENV CSV=False
ENV CCDA=True
ENV DSTU2=True
ENV STU3=True
ENV R4=True

#* Download Synthea
RUN wget --quiet "https://github.com/synthetichealth/synthea/releases/download/${SYNTHEA_BRANCH}/${SYNTHEA_FILE}.jar"

#* Execution
COPY entrypoint.sh entrypoint.sh
RUN chmod 755 entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
