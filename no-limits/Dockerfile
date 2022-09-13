FROM python
ADD  entrypoint.sh hello-world.py /code/
RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
CMD ["start"]
