FROM jupyter/tensorflow-notebook:ae5f7e104dd5

WORKDIR /jupyter

COPY environment.yml ./
RUN conda env create -f environment.yml
RUN echo "source activate jupyter" >> ~/.bashrc

WORKDIR /notebooks

CMD [ "conda", "run", "-njupyter", "jupyter", "notebook", "--NotebookApp.token=''"]