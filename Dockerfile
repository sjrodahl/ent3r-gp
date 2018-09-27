# Alpine is a lightweight python image
FROM python:3.5-alpine

# Arbitrary location to store code in the container
RUN mkdir -p /opt/services/djangoapp/src

# Copy project files over to the container
COPY . /opt/services/djangoapp/src

WORKDIR /opt/services/djangoapp/src

# Install python requirements
RUN pip install -r requirements.txt

# Not sure if clearing files are necessary
RUN cd ent3r_gp && python manage.py collectstatic --clear --noinput
RUN cd ent3r_gp && python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "--chdir", "ent3r_gp", "--bind", ":8000", "ent3r_gp.wsgi:application"]
