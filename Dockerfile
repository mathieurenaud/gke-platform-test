FROM centos
EXPOSE 8000
RUN mkdir -p /var/lib/myapp
COPY src/app.py /var/lib/myapp/
CMD python /var/lib/myapp/app.py

