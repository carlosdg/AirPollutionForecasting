FROM jupyter/tensorflow-notebook:ae5f7e104dd5

WORKDIR /home/api

COPY environment.yml ./
RUN conda env create -f environment.yml
RUN echo "source activate api" >> ~/.bashrc

ENV PATH /opt/conda/envs/api/bin:$PATH
ENV CONDA_DEFAULT_ENV api

COPY . /home/api

CMD [ "python", "src/api.py" ]