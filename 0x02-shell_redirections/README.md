I/O Redirections and Filters project
1. script that prints “Hello, World”, followed by a new line to the standard output: echo Hello, World
2. script that displays a confused smiley "(Ôo)': echo "\"(Oo)'"
3. Display the content of the /etc/passwd file: cat /etc/passwd
4. Display the content of /etc/passwd and /etc/hosts
5. Display the last 10 lines of /etc/passwd: tail -n 10 /etc/passwd
6. Display the first 10 lines of /etc/passwd: head -n 10 /etc/passwd
7. Script that displays the third line of the file iacta: head -n 3 iacta | tail -n 1
8. shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line: echo "Best School" > "\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)"
9. script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it: ls -ls > ls_cwd_content
