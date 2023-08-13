# Copyright (c) Datalayer, Inc. https://datalayer.io
# Distributed under the terms of the MIT License.

FROM python:3.11

RUN mkdir /opt/jupyter-run

WORKDIR /opt/jupyter-run

RUN pip install kazoo

COPY jupyter_run /opt/jupyter_run
RUN pip install -e ./jupyter_run

# COPY frontplane/dist.html /opt/jupyter-run/index.html

WORKDIR /opt/jupyter-run/editor

EXPOSE 9300

CMD ["python", "-m", "jupyter_run"]
