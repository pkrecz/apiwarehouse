FROM python:3.12-bookworm

ARG STATIC_ROOT

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/home/apiwarehouse
ENV WDIR=$APP_HOME/app

RUN mkdir $APP_HOME
RUN mkdir $WDIR
RUN mkdir $WDIR/$STATIC_ROOT

WORKDIR $WDIR

COPY requirements.txt $WDIR

RUN pip install --no-cache-dir -r $WDIR/requirements.txt
RUN apt-get update

COPY . $WDIR/

CMD ["gunicorn", "apiwhsproject.wsgi:application"]
