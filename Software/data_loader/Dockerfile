FROM jupyter/tensorflow-notebook:ae5f7e104dd5

WORKDIR /home/data_loader

COPY environment.yml ./
RUN conda env create -f environment.yml
RUN echo "source activate data_loader" >> ~/.bashrc

CMD [ "/bin/bash" ]