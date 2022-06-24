Shell permissions readme
0.Script that switches current user to betty: su betty
1.Script that prints effective username for current user: whoami
2.Script that prints all the groups the current user is part of.
3.Script that changes the owner of the file hello to the user betty: chown betty hello
4.Script that creates an empty file called hello: touch hello
5.script that adds execute permission to the owner of the file hello: chmod 744 hello
6.script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello: chmod 754 hello
7.script that adds execution permission to the owner, the group owner and the other users, to the file hello: chmod 751 hello
8.script that sets the permission to the file hello as follows:Owner: no permission at all,Group: no permission at all,Other users: all the permissions: chmod 007 hello
9.script that sets the mode of the file hello to -rwxr-x-wx: chmod 753 hello
10.script that sets the mode of the file hello the same as olleh’s mode.: chmod --reference=olleh hello
11.
12.script that creates a directory called my_dir with permissions 751 in the working directoryo.
13.
14.script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory: chown vincent:staff *
15.script that changes the owner and the group owner of _hello to vincent and staff respectively:_hello is in the working directory and it is a symbolic link: chown -h vincent:staff _hello: -h flag ensures that the chown is applied on the link alone, not to the related files too.
16.script that changes the owner of the file hello to betty only if it is owned by the user guillaume: chown --from=guillaume betty hello
17.script that will play the StarWars IV episode in the terminal: cat < /dev/tcp/towel.blinkenlights.nl/23
