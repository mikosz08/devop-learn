FROM debian:sid
# update dependences
RUN apt-get -y update
# install nano
RUN apt-get -y install nano
# using nano make and edit a file
CMD ["/bin/nano", "/tmp/notes"]