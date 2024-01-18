# 0x00. MySQL advanced
<div class="panel panel-default" id="project-description" style="box-sizing: border-box; margin-bottom: 20px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel-body" style="box-sizing: border-box; padding: 15px;">
        <h2 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 30px;">Resources</h2>
        <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Read or watch</strong>:</p>
        <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
            <li style="box-sizing: border-box;"><a href="https://intranet.alxswe.com/rltoken/8w9di_hk19DIMSBEV3EayQ" title="MySQL cheatsheet" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">MySQL cheatsheet</a></li>
            <li
            style="box-sizing: border-box;"><a href="https://intranet.alxswe.com/rltoken/2GJbZ48zRPA70o2YhTdH7g" title="MySQL Performance: How To Leverage MySQL Database Indexing" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">MySQL Performance: How To Leverage MySQL Database Indexing</a></li>
                <li
                style="box-sizing: border-box;"><a href="https://intranet.alxswe.com/rltoken/K180X2OCzb6gzPngjn-EIg" title="Stored Procedure" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">Stored Procedure</a></li>
                    <li
                    style="box-sizing: border-box;"><a href="https://intranet.alxswe.com/rltoken/cJ1qA4o-rRm4rWIsqYKSZg" title="Triggers" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">Triggers</a></li>
                        <li
                        style="box-sizing: border-box;"><a href="https://intranet.alxswe.com/rltoken/vHg1z3UAOcWMvOt8xZHeiA" title="Views" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">Views</a></li>
                            <li
                            style="box-sizing: border-box;"><a href="https://intranet.alxswe.com/rltoken/g-c1m6iljScpi4LeqxBRqQ" title="Functions and Operators" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">Functions and Operators</a></li>
                                <li
                                style="box-sizing: border-box;"><a href="https://intranet.alxswe.com/rltoken/gLVwKjQfRL0Jr_nWqAS7VQ" title="Trigger Syntax and Examples" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">Trigger Syntax and Examples</a></li>
                                    <li
                                    style="box-sizing: border-box;"><a href="https://intranet.alxswe.com/rltoken/X789nJ22H6HVh1uCQPl0lg" title="CREATE TABLE Statement" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">CREATE TABLE Statement</a></li>
                                        <li
                                        style="box-sizing: border-box;"><a href="https://intranet.alxswe.com/rltoken/mfrWMt1KL3NHXblJykMgZg" title="CREATE PROCEDURE and CREATE FUNCTION Statements" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">CREATE PROCEDURE and CREATE FUNCTION Statements</a></li>
                                            <li
                                            style="box-sizing: border-box;"><a href="https://intranet.alxswe.com/rltoken/oCu8Rg9WfKyF4BhTt8dZGQ" title="CREATE INDEX Statement" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">CREATE INDEX Statement</a></li>
                                                <li
                                                style="box-sizing: border-box;"><a href="https://intranet.alxswe.com/rltoken/FEZNlZFKZmD1ISnLINkCwQ" title="CREATE VIEW Statement" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">CREATE VIEW Statement</a></li>
        </ul>
        <h2 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 30px;">Learning Objectives</h2>
        <p style="box-sizing: border-box; margin: 0px 0px 10px;">At the end of this project, you are expected to be able to<span> </span><a href="https://intranet.alxswe.com/rltoken/NEA0Fr7muHfukl5lziVAhg" title="explain to anyone" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">explain to anyone</a>,<span> </span>
            <strong
            style="box-sizing: border-box; font-weight: bold;">without the help of Google</strong>:</p>
        <h3 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 24px;">General</h3>
        <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
            <li style="box-sizing: border-box;">How to create tables with constraints</li>
            <li style="box-sizing: border-box;">How to optimize queries by adding indexes</li>
            <li style="box-sizing: border-box;">What is and how to implement stored procedures and functions in MySQL</li>
            <li style="box-sizing: border-box;">What is and how to implement views in MySQL</li>
            <li style="box-sizing: border-box;">What is and how to implement triggers in MySQL</li>
        </ul>
        <h2 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 30px;">Requirements</h2>
        <h3 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 24px;">General</h3>
        <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
            <li style="box-sizing: border-box;">All your files will be executed on Ubuntu 18.04 LTS using<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">MySQL 5.7</code><span> </span>(version
                5.7.30)</li>
            <li style="box-sizing: border-box;">All your files should end with a new line</li>
            <li style="box-sizing: border-box;">All your SQL queries should have a comment just before (i.e. syntax above)</li>
            <li style="box-sizing: border-box;">All your files should start by a comment describing the task</li>
            <li style="box-sizing: border-box;">All SQL keywords should be in uppercase (<code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">SELECT</code>,<span> </span>
                <code
                style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">WHERE</code>…)</li>
            <li style="box-sizing: border-box;">A<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">README.md</code><span> </span>file,
                at the root of the folder of the project, is mandatory</li>
            <li style="box-sizing: border-box;">The length of your files will be tested using<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">wc</code></li>
        </ul>
        <h2 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 30px;">More Info</h2>
        <h3 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 24px;">Comments for your SQL file:</h3><pre style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>
        <h3 style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 24px;">Use “container-on-demand” to run MySQL</h3>
        <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
            <li style="box-sizing: border-box;">Ask for container<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">Ubuntu 18.04 - Python 3.7</code></li>
            <li
            style="box-sizing: border-box;">Connect via SSH</li>
                <li style="box-sizing: border-box;">Or via the WebTerminal</li>
                <li style="box-sizing: border-box;">In the container, you should start MySQL before playing with it:</li>
        </ul><pre style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
</code></pre>
        <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">In the container, credentials are<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">root/root</code></strong></p>
        <h3
        style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: inherit; margin-top: 20px; margin-bottom: 10px; font-size: 24px;">How to import a SQL dump</h3><pre style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
</code></pre></div>
</div>
<h2 class="gap" style="box-sizing: border-box; font-family: aktiv-grotesk, sans-serif; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 50px !important; margin-bottom: 10px; font-size: 30px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">Tasks</h2>
<div data-role="task11633" data-position="1" id="task-num-0" style="box-sizing: border-box; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel panel-default task-card " id="task-11633" style="box-sizing: border-box; margin-bottom: 50px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
        <div class="panel-heading panel-heading-actions" style="box-sizing: border-box; padding: 10px 15px; border-bottom: 1px solid rgb(221, 221, 221); border-top-left-radius: 3px; border-top-right-radius: 3px; color: rgb(51, 51, 51); background-color: rgb(245, 245, 245); border-top-color: rgb(221, 221, 221); border-right-color: rgb(221, 221, 221); border-left-color: rgb(221, 221, 221); align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between;">
            <h3 class="panel-title" style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 0px; margin-bottom: 0px; font-size: 16px;">0. We are all unique!</h3>
            <div style="box-sizing: border-box; display: flex;"><span class="label label-info" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 10.5px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(152, 163, 174);">mandatory</span></div>
        </div>
        <div class="panel-body" style="box-sizing: border-box; padding: 15px;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Write a SQL script that creates a table<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">users</code><span> </span>following
                these requirements:</p>
            <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                <li style="box-sizing: border-box;">With these attributes:
                    <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 0px;">
                        <li style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">id</code>,
                            integer, never null, auto increment and primary key</li>
                        <li style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">email</code>,
                            string (255 characters), never null and unique</li>
                        <li style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">name</code>,
                            string (255 characters)</li>
                    </ul>
                </li>
                <li style="box-sizing: border-box;">If the table already exists, your script should not fail</li>
                <li style="box-sizing: border-box;">Your script can be executed on any database</li>
            </ul>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Context:</strong><span> </span><em style="box-sizing: border-box;">Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application</em></p>
            <pre
            style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$ 
</code></pre>
        </div>
        <div class="list-group" style="box-sizing: border-box; padding-left: 0px; margin-bottom: 0px;">
            <div class="list-group-item" style="box-sizing: border-box; position: relative; display: block; padding: 10px 15px; margin-bottom: 0px; background-color: rgb(255, 255, 255); border-width: 1px 0px; border-style: solid; border-color: rgb(221, 221, 221); border-image: initial; border-radius: 0px;">
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Repo:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">GitHub repository:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">alx-backend-storage</code></li>
                    <li
                    style="box-sizing: border-box;">Directory:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0x00-MySQL_Advanced</code></li>
                        <li
                        style="box-sizing: border-box;">File:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0-uniq_users.sql</code></li>
                </ul>
            </div>
        </div>
        <div class="panel-footer" style="box-sizing: border-box; padding: 10px 15px; background-color: rgb(245, 245, 245); border-top: 0px solid rgb(221, 221, 221); border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">
            <div class="align-items-center d-flex justify-content-between" style="box-sizing: border-box; align-items: center !important; display: flex !important; justify-content: space-between !important;">
                <div style="box-sizing: border-box;">
                    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11633" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><span class="no" style="box-sizing: border-box; display: inline;"><i aria-hidden="true" class="fa-regular fa-square " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 400;"></i></span><span> </span>Done
                        <span
                        class="no pending" style="box-sizing: border-box; display: inline;">?</span>
                    </button><span> </span>
                    <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11633" data-batch-id="74" data-toggle="modal" data-target="#task-11633-users-done-modal" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Help</button><span> </span>
                    <button class="btn btn-default btn-sm check-your-task-11633-modal-button" data-task-id="11633" data-toggle="modal" data-target="#task-test-correction-11633-correction-modal" id="task-num-0-check-code-btn"
                    data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11633}" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Check your code</button><span> </span>
                    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11633}"
                    style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><i aria-hidden="true" class="fa-solid fa-terminal " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 900; margin-right: 5px;"></i>
                        <span
                        style="box-sizing: border-box;">Get a sandbox</span>
                    </button>
                </div>
                <div class="fs-4" style="box-sizing: border-box; font-size: 1.5rem !important;"></div>
            </div>
        </div>
    </div>
</div>
<div data-role="task11634" data-position="2" id="task-num-1" style="box-sizing: border-box; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel panel-default task-card " id="task-11634" style="box-sizing: border-box; margin-bottom: 50px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
        <div class="panel-heading panel-heading-actions" style="box-sizing: border-box; padding: 10px 15px; border-bottom: 1px solid rgb(221, 221, 221); border-top-left-radius: 3px; border-top-right-radius: 3px; color: rgb(51, 51, 51); background-color: rgb(245, 245, 245); border-top-color: rgb(221, 221, 221); border-right-color: rgb(221, 221, 221); border-left-color: rgb(221, 221, 221); align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between;">
            <h3 class="panel-title" style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 0px; margin-bottom: 0px; font-size: 16px;">1. In and not out</h3>
            <div style="box-sizing: border-box; display: flex;"><span class="label label-info" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 10.5px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(152, 163, 174);">mandatory</span></div>
        </div>
        <div class="panel-body" style="box-sizing: border-box; padding: 15px;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Write a SQL script that creates a table<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">users</code><span> </span>following
                these requirements:</p>
            <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                <li style="box-sizing: border-box;">With these attributes:
                    <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 0px;">
                        <li style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">id</code>,
                            integer, never null, auto increment and primary key</li>
                        <li style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">email</code>,
                            string (255 characters), never null and unique</li>
                        <li style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">name</code>,
                            string (255 characters)</li>
                        <li style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">country</code>,
                            enumeration of countries:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">US</code>,<span> </span>
                            <code
                            style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">CO</code><span> </span>and<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">TN</code>,
                                never null (= default will be the first element of the enumeration, here<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">US</code>)</li>
                    </ul>
                </li>
                <li style="box-sizing: border-box;">If the table already exists, your script should not fail</li>
                <li style="box-sizing: border-box;">Your script can be executed on any database</li>
            </ul><pre style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 1-country_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password: 
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
bob@dylan:~$ 
</code></pre></div>
        <div class="list-group" style="box-sizing: border-box; padding-left: 0px; margin-bottom: 0px;">
            <div class="list-group-item" style="box-sizing: border-box; position: relative; display: block; padding: 10px 15px; margin-bottom: 0px; background-color: rgb(255, 255, 255); border-width: 1px 0px; border-style: solid; border-color: rgb(221, 221, 221); border-image: initial; border-radius: 0px;">
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Repo:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">GitHub repository:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">alx-backend-storage</code></li>
                    <li
                    style="box-sizing: border-box;">Directory:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0x00-MySQL_Advanced</code></li>
                        <li
                        style="box-sizing: border-box;">File:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">1-country_users.sql</code></li>
                </ul>
            </div>
        </div>
        <div class="panel-footer" style="box-sizing: border-box; padding: 10px 15px; background-color: rgb(245, 245, 245); border-top: 0px solid rgb(221, 221, 221); border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">
            <div class="align-items-center d-flex justify-content-between" style="box-sizing: border-box; align-items: center !important; display: flex !important; justify-content: space-between !important;">
                <div style="box-sizing: border-box;">
                    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11634" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><span class="no" style="box-sizing: border-box; display: inline;"><i aria-hidden="true" class="fa-regular fa-square " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 400;"></i></span><span> </span>Done
                        <span
                        class="no pending" style="box-sizing: border-box; display: inline;">?</span>
                    </button><span> </span>
                    <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11634" data-batch-id="74" data-toggle="modal" data-target="#task-11634-users-done-modal" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Help</button><span> </span>
                    <button class="btn btn-default btn-sm check-your-task-11634-modal-button" data-task-id="11634" data-toggle="modal" data-target="#task-test-correction-11634-correction-modal" id="task-num-1-check-code-btn"
                    data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11634}" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Check your code</button><span> </span>
                    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11634}"
                    style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><i aria-hidden="true" class="fa-solid fa-terminal " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 900; margin-right: 5px;"></i>
                        <span
                        style="box-sizing: border-box;">Get a sandbox</span>
                    </button>
                </div>
                <div class="fs-4" style="box-sizing: border-box; font-size: 1.5rem !important;"></div>
            </div>
        </div>
    </div>
</div>
<div data-role="task11635" data-position="3" id="task-num-2" style="box-sizing: border-box; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel panel-default task-card " id="task-11635" style="box-sizing: border-box; margin-bottom: 50px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
        <div class="panel-heading panel-heading-actions" style="box-sizing: border-box; padding: 10px 15px; border-bottom: 1px solid rgb(221, 221, 221); border-top-left-radius: 3px; border-top-right-radius: 3px; color: rgb(51, 51, 51); background-color: rgb(245, 245, 245); border-top-color: rgb(221, 221, 221); border-right-color: rgb(221, 221, 221); border-left-color: rgb(221, 221, 221); align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between;">
            <h3 class="panel-title" style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 0px; margin-bottom: 0px; font-size: 16px;">2. Best band ever!</h3>
            <div style="box-sizing: border-box; display: flex;"><span class="label label-info" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 10.5px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(152, 163, 174);">mandatory</span></div>
        </div>
        <div class="panel-body" style="box-sizing: border-box; padding: 15px;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans</p>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Requirements:</strong></p>
            <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                <li style="box-sizing: border-box;">Import this table dump:<span> </span><a href="https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ" title="metal_bands.sql.zip" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">metal_bands.sql.zip</a></li>
                <li
                style="box-sizing: border-box;">Column names must be:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">origin</code><span> </span>and<span> </span>
                    <code
                    style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">nb_fans</code>
                        </li>
                        <li style="box-sizing: border-box;">Your script can be executed on any database</li>
            </ul>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Context:</strong><span> </span><em style="box-sizing: border-box;">Calculate/compute something is always power intensive… better to distribute the load!</em></p><pre style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 2-fans.sql | mysql -uroot -p holberton &gt; tmp_res ; head tmp_res
Enter password: 
origin  nb_fans
USA 99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
bob@dylan:~$ 
</code></pre></div>
        <div class="list-group" style="box-sizing: border-box; padding-left: 0px; margin-bottom: 0px;">
            <div class="list-group-item" style="box-sizing: border-box; position: relative; display: block; padding: 10px 15px; margin-bottom: 0px; background-color: rgb(255, 255, 255); border-width: 1px 0px; border-style: solid; border-color: rgb(221, 221, 221); border-image: initial; border-radius: 0px;">
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Repo:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">GitHub repository:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">alx-backend-storage</code></li>
                    <li
                    style="box-sizing: border-box;">Directory:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0x00-MySQL_Advanced</code></li>
                        <li
                        style="box-sizing: border-box;">File:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">2-fans.sql</code></li>
                </ul>
            </div>
        </div>
        <div class="panel-footer" style="box-sizing: border-box; padding: 10px 15px; background-color: rgb(245, 245, 245); border-top: 0px solid rgb(221, 221, 221); border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">
            <div class="align-items-center d-flex justify-content-between" style="box-sizing: border-box; align-items: center !important; display: flex !important; justify-content: space-between !important;">
                <div style="box-sizing: border-box;">
                    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11635" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><span class="no" style="box-sizing: border-box; display: inline;"><i aria-hidden="true" class="fa-regular fa-square " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 400;"></i></span><span> </span>Done
                        <span
                        class="no pending" style="box-sizing: border-box; display: inline;">?</span>
                    </button><span> </span>
                    <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11635" data-batch-id="74" data-toggle="modal" data-target="#task-11635-users-done-modal" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Help</button><span> </span>
                    <button class="btn btn-default btn-sm check-your-task-11635-modal-button" data-task-id="11635" data-toggle="modal" data-target="#task-test-correction-11635-correction-modal" id="task-num-2-check-code-btn"
                    data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11635}" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Check your code</button><span> </span>
                    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11635}"
                    style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><i aria-hidden="true" class="fa-solid fa-terminal " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 900; margin-right: 5px;"></i>
                        <span
                        style="box-sizing: border-box;">Get a sandbox</span>
                    </button>
                </div>
                <div class="fs-4" style="box-sizing: border-box; font-size: 1.5rem !important;"></div>
            </div>
        </div>
    </div>
</div>
<div data-role="task11636" data-position="4" id="task-num-3" style="box-sizing: border-box; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel panel-default task-card " id="task-11636" style="box-sizing: border-box; margin-bottom: 50px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
        <div class="panel-heading panel-heading-actions" style="box-sizing: border-box; padding: 10px 15px; border-bottom: 1px solid rgb(221, 221, 221); border-top-left-radius: 3px; border-top-right-radius: 3px; color: rgb(51, 51, 51); background-color: rgb(245, 245, 245); border-top-color: rgb(221, 221, 221); border-right-color: rgb(221, 221, 221); border-left-color: rgb(221, 221, 221); align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between;">
            <h3 class="panel-title" style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 0px; margin-bottom: 0px; font-size: 16px;">3. Old school band</h3>
            <div style="box-sizing: border-box; display: flex;"><span class="label label-info" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 10.5px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(152, 163, 174);">mandatory</span></div>
        </div>
        <div class="panel-body" style="box-sizing: border-box; padding: 15px;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Write a SQL script that lists all bands with<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">Glam rock</code><span> </span>as
                their main style, ranked by their longevity</p>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Requirements:</strong></p>
            <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                <li style="box-sizing: border-box;">Import this table dump:<span> </span><a href="https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ" title="metal_bands.sql.zip" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">metal_bands.sql.zip</a></li>
                <li
                style="box-sizing: border-box;">Column names must be:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">band_name</code><span> </span>and<span> </span>
                    <code
                    style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">lifespan</code><span> </span>(in years<span> </span><strong style="box-sizing: border-box; font-weight: bold;">until 2022</strong><span> </span>- please use<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">2022</code><span> </span>instead
                        of<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">YEAR(CURDATE())</code>)</li>
                        <li
                        style="box-sizing: border-box;">You should use attributes<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">formed</code><span> </span>and<span> </span>
                            <code
                            style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">split</code><span> </span>for computing the<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">lifespan</code></li>
                                <li
                                style="box-sizing: border-box;">Your script can be executed on any database</li>
            </ul><pre style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 3-glam_rock.sql | mysql -uroot -p holberton 
Enter password: 
band_name   lifespan
Alice Cooper    56
Mötley Crüe   34
Marilyn Manson  31
The 69 Eyes 30
Hardcore Superstar  23
Nasty Idols 0
Hanoi Rocks 0
bob@dylan:~$ 
</code></pre></div>
        <div class="list-group" style="box-sizing: border-box; padding-left: 0px; margin-bottom: 0px;">
            <div class="list-group-item" style="box-sizing: border-box; position: relative; display: block; padding: 10px 15px; margin-bottom: 0px; background-color: rgb(255, 255, 255); border-width: 1px 0px; border-style: solid; border-color: rgb(221, 221, 221); border-image: initial; border-radius: 0px;">
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Repo:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">GitHub repository:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">alx-backend-storage</code></li>
                    <li
                    style="box-sizing: border-box;">Directory:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0x00-MySQL_Advanced</code></li>
                        <li
                        style="box-sizing: border-box;">File:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">3-glam_rock.sql</code></li>
                </ul>
            </div>
        </div>
        <div class="panel-footer" style="box-sizing: border-box; padding: 10px 15px; background-color: rgb(245, 245, 245); border-top: 0px solid rgb(221, 221, 221); border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">
            <div class="align-items-center d-flex justify-content-between" style="box-sizing: border-box; align-items: center !important; display: flex !important; justify-content: space-between !important;">
                <div style="box-sizing: border-box;">
                    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11636" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><span class="no" style="box-sizing: border-box; display: inline;"><i aria-hidden="true" class="fa-regular fa-square " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 400;"></i></span><span> </span>Done
                        <span
                        class="no pending" style="box-sizing: border-box; display: inline;">?</span>
                    </button><span> </span>
                    <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11636" data-batch-id="74" data-toggle="modal" data-target="#task-11636-users-done-modal" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Help</button><span> </span>
                    <button class="btn btn-default btn-sm check-your-task-11636-modal-button" data-task-id="11636" data-toggle="modal" data-target="#task-test-correction-11636-correction-modal" id="task-num-3-check-code-btn"
                    data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11636}" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Check your code</button><span> </span>
                    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11636}"
                    style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><i aria-hidden="true" class="fa-solid fa-terminal " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 900; margin-right: 5px;"></i>
                        <span
                        style="box-sizing: border-box;">Get a sandbox</span>
                    </button>
                </div>
                <div class="fs-4" style="box-sizing: border-box; font-size: 1.5rem !important;"></div>
            </div>
        </div>
    </div>
</div>
<div data-role="task11637" data-position="5" id="task-num-4" style="box-sizing: border-box; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel panel-default task-card " id="task-11637" style="box-sizing: border-box; margin-bottom: 50px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
        <div class="panel-heading panel-heading-actions" style="box-sizing: border-box; padding: 10px 15px; border-bottom: 1px solid rgb(221, 221, 221); border-top-left-radius: 3px; border-top-right-radius: 3px; color: rgb(51, 51, 51); background-color: rgb(245, 245, 245); border-top-color: rgb(221, 221, 221); border-right-color: rgb(221, 221, 221); border-left-color: rgb(221, 221, 221); align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between;">
            <h3 class="panel-title" style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 0px; margin-bottom: 0px; font-size: 16px;">4. Buy buy buy</h3>
            <div style="box-sizing: border-box; display: flex;"><span class="label label-info" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 10.5px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(152, 163, 174);">mandatory</span></div>
        </div>
        <div class="panel-body" style="box-sizing: border-box; padding: 15px;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.</p>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Quantity in the table<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">items</code><span> </span>can
                be negative.</p>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Context:</strong><span> </span><em style="box-sizing: border-box;">Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!</em></p>
            <pre
            style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">bob@dylan:~$ cat 4-init.sql
-- Initial
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity int NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
    item_name VARCHAR(255) NOT NULL,
    number int NOT NULL
);

INSERT INTO items (name) VALUES ("apple"), ("pineapple"), ("pear");

bob@dylan:~$ 
bob@dylan:~$ cat 4-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 4-store.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 4-main.sql
Enter password: 
-- Show and add orders
SELECT * FROM items;
SELECT * FROM orders;

INSERT INTO orders (item_name, number) VALUES ('apple', 1);
INSERT INTO orders (item_name, number) VALUES ('apple', 3);
INSERT INTO orders (item_name, number) VALUES ('pear', 2);

SELECT "--";

SELECT * FROM items;
SELECT * FROM orders;

bob@dylan:~$ 
bob@dylan:~$ cat 4-main.sql | mysql -uroot -p holberton 
Enter password: 
name    quantity
apple   10
pineapple   10
pear    10
--
--
name    quantity
apple   6
pineapple   10
pear    8
item_name   number
apple   1
apple   3
pear    2
bob@dylan:~$ 
</code></pre>
        </div>
        <div class="list-group" style="box-sizing: border-box; padding-left: 0px; margin-bottom: 0px;">
            <div class="list-group-item" style="box-sizing: border-box; position: relative; display: block; padding: 10px 15px; margin-bottom: 0px; background-color: rgb(255, 255, 255); border-width: 1px 0px; border-style: solid; border-color: rgb(221, 221, 221); border-image: initial; border-radius: 0px;">
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Repo:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">GitHub repository:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">alx-backend-storage</code></li>
                    <li
                    style="box-sizing: border-box;">Directory:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0x00-MySQL_Advanced</code></li>
                        <li
                        style="box-sizing: border-box;">File:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">4-store.sql</code></li>
                </ul>
            </div>
        </div>
        <div class="panel-footer" style="box-sizing: border-box; padding: 10px 15px; background-color: rgb(245, 245, 245); border-top: 0px solid rgb(221, 221, 221); border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">
            <div class="align-items-center d-flex justify-content-between" style="box-sizing: border-box; align-items: center !important; display: flex !important; justify-content: space-between !important;">
                <div style="box-sizing: border-box;">
                    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11637" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><span class="no" style="box-sizing: border-box; display: inline;"><i aria-hidden="true" class="fa-regular fa-square " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 400;"></i></span><span> </span>Done
                        <span
                        class="no pending" style="box-sizing: border-box; display: inline;">?</span>
                    </button><span> </span>
                    <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11637" data-batch-id="74" data-toggle="modal" data-target="#task-11637-users-done-modal" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Help</button><span> </span>
                    <button class="btn btn-default btn-sm check-your-task-11637-modal-button" data-task-id="11637" data-toggle="modal" data-target="#task-test-correction-11637-correction-modal" id="task-num-4-check-code-btn"
                    data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11637}" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Check your code</button><span> </span>
                    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11637}"
                    style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><i aria-hidden="true" class="fa-solid fa-terminal " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 900; margin-right: 5px;"></i>
                        <span
                        style="box-sizing: border-box;">Get a sandbox</span>
                    </button>
                </div>
                <div class="fs-4" style="box-sizing: border-box; font-size: 1.5rem !important;"></div>
            </div>
        </div>
    </div>
</div>
<div data-role="task11638" data-position="6" id="task-num-5" style="box-sizing: border-box; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel panel-default task-card " id="task-11638" style="box-sizing: border-box; margin-bottom: 50px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
        <div class="panel-heading panel-heading-actions" style="box-sizing: border-box; padding: 10px 15px; border-bottom: 1px solid rgb(221, 221, 221); border-top-left-radius: 3px; border-top-right-radius: 3px; color: rgb(51, 51, 51); background-color: rgb(245, 245, 245); border-top-color: rgb(221, 221, 221); border-right-color: rgb(221, 221, 221); border-left-color: rgb(221, 221, 221); align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between;">
            <h3 class="panel-title" style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 0px; margin-bottom: 0px; font-size: 16px;">5. Email validation to sent</h3>
            <div style="box-sizing: border-box; display: flex;"><span class="label label-info" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 10.5px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(152, 163, 174);">mandatory</span></div>
        </div>
        <div class="panel-body" style="box-sizing: border-box; padding: 15px;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Write a SQL script that creates a trigger that resets the attribute<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">valid_email</code><span> </span>only
                when the<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">email</code><span> </span>has
                been changed.</p>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Context:</strong><span> </span><em style="box-sizing: border-box;">Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!</em></p>
            <pre
            style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">bob@dylan:~$ cat 5-init.sql
-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    email varchar(255) not null,
    name varchar(255),
    valid_email boolean not null default 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name, valid_email) VALUES ("sylvie@dylan.com", "Sylvie", 1);
INSERT INTO users (email, name, valid_email) VALUES ("jeanne@dylan.com", "Jeanne", 1);

bob@dylan:~$ 
bob@dylan:~$ cat 5-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 5-valid_email.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 5-main.sql
Enter password: 
-- Show users and update (or not) email
SELECT * FROM users;

UPDATE users SET valid_email = 1 WHERE email = "bob@dylan.com";
UPDATE users SET email = "sylvie+new@dylan.com" WHERE email = "sylvie@dylan.com";
UPDATE users SET name = "Jannis" WHERE email = "jeanne@dylan.com";

SELECT "--";
SELECT * FROM users;

UPDATE users SET email = "bob@dylan.com" WHERE email = "bob@dylan.com";

SELECT "--";
SELECT * FROM users;

bob@dylan:~$ 
bob@dylan:~$ cat 5-main.sql | mysql -uroot -p holberton 
Enter password: 
id  email   name    valid_email
1   bob@dylan.com   Bob 0
2   sylvie@dylan.com    Sylvie  1
3   jeanne@dylan.com    Jeanne  1
--
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
--
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
bob@dylan:~$ 
</code></pre>
        </div>
        <div class="list-group" style="box-sizing: border-box; padding-left: 0px; margin-bottom: 0px;">
            <div class="list-group-item" style="box-sizing: border-box; position: relative; display: block; padding: 10px 15px; margin-bottom: 0px; background-color: rgb(255, 255, 255); border-width: 1px 0px; border-style: solid; border-color: rgb(221, 221, 221); border-image: initial; border-radius: 0px;">
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Repo:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">GitHub repository:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">alx-backend-storage</code></li>
                    <li
                    style="box-sizing: border-box;">Directory:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0x00-MySQL_Advanced</code></li>
                        <li
                        style="box-sizing: border-box;">File:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">5-valid_email.sql</code></li>
                </ul>
            </div>
        </div>
        <div class="panel-footer" style="box-sizing: border-box; padding: 10px 15px; background-color: rgb(245, 245, 245); border-top: 0px solid rgb(221, 221, 221); border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">
            <div class="align-items-center d-flex justify-content-between" style="box-sizing: border-box; align-items: center !important; display: flex !important; justify-content: space-between !important;">
                <div style="box-sizing: border-box;">
                    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11638" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><span class="no" style="box-sizing: border-box; display: inline;"><i aria-hidden="true" class="fa-regular fa-square " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 400;"></i></span><span> </span>Done
                        <span
                        class="no pending" style="box-sizing: border-box; display: inline;">?</span>
                    </button><span> </span>
                    <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11638" data-batch-id="74" data-toggle="modal" data-target="#task-11638-users-done-modal" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Help</button><span> </span>
                    <button class="btn btn-default btn-sm check-your-task-11638-modal-button" data-task-id="11638" data-toggle="modal" data-target="#task-test-correction-11638-correction-modal" id="task-num-5-check-code-btn"
                    data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11638}" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Check your code</button><span> </span>
                    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11638}"
                    style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><i aria-hidden="true" class="fa-solid fa-terminal " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 900; margin-right: 5px;"></i>
                        <span
                        style="box-sizing: border-box;">Get a sandbox</span>
                    </button>
                </div>
                <div class="fs-4" style="box-sizing: border-box; font-size: 1.5rem !important;"></div>
            </div>
        </div>
    </div>
</div>
<div data-role="task11639" data-position="7" id="task-num-6" style="box-sizing: border-box; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel panel-default task-card " id="task-11639" style="box-sizing: border-box; margin-bottom: 50px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
        <div class="panel-heading panel-heading-actions" style="box-sizing: border-box; padding: 10px 15px; border-bottom: 1px solid rgb(221, 221, 221); border-top-left-radius: 3px; border-top-right-radius: 3px; color: rgb(51, 51, 51); background-color: rgb(245, 245, 245); border-top-color: rgb(221, 221, 221); border-right-color: rgb(221, 221, 221); border-left-color: rgb(221, 221, 221); align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between;">
            <h3 class="panel-title" style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 0px; margin-bottom: 0px; font-size: 16px;">6. Add bonus</h3>
            <div style="box-sizing: border-box; display: flex;"><span class="label label-info" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 10.5px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(152, 163, 174);">mandatory</span></div>
        </div>
        <div class="panel-body" style="box-sizing: border-box; padding: 15px;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Write a SQL script that creates a stored procedure<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">AddBonus</code><span> </span>that
                adds a new correction for a student.</p>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Requirements:</strong></p>
            <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                <li style="box-sizing: border-box;">Procedure<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">AddBonus</code><span> </span>is
                    taking 3 inputs (in this order):
                    <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 0px;">
                        <li style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">user_id</code>,
                            a<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">users.id</code><span> </span>value
                            (you can assume<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">user_id</code><span> </span>is
                            linked to an existing<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">users</code>)</li>
                        <li
                        style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">project_name</code>,
                            a new or already exists<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">projects</code><span> </span>-
                            if no<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">projects.name</code><span> </span>found
                            in the table, you should create it</li>
                <li style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">score</code>,
                    the score value for the correction</li>
                </ul>
                </li>
            </ul>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Context:</strong><span> </span><em style="box-sizing: border-box;">Write code in SQL is a nice level up!</em></p><pre style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">bob@dylan:~$ cat 6-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    average_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id int not null,
    project_id int not null,
    score int default 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES ("C is fun");
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project_py = LAST_INSERT_ID();


INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$ 
bob@dylan:~$ cat 6-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 6-bonus.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 6-main.sql
Enter password: 
-- Show and add bonus correction
SELECT * FROM projects;
SELECT * FROM corrections;

SELECT "--";

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "Python is cool", 100);

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "Bonus project", 100);
CALL AddBonus((SELECT id FROM users WHERE name = "Bob"), "Bonus project", 10);

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "New bonus", 90);

SELECT "--";

SELECT * FROM projects;
SELECT * FROM corrections;

bob@dylan:~$ 
bob@dylan:~$ cat 6-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name
1   C is fun
2   Python is cool
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name
1   C is fun
2   Python is cool
3   Bonus project
4   New bonus
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
2   2   100
2   3   100
1   3   10
2   4   90
bob@dylan:~$ 
</code></pre></div>
        <div class="list-group" style="box-sizing: border-box; padding-left: 0px; margin-bottom: 0px;">
            <div class="list-group-item" style="box-sizing: border-box; position: relative; display: block; padding: 10px 15px; margin-bottom: 0px; background-color: rgb(255, 255, 255); border-width: 1px 0px; border-style: solid; border-color: rgb(221, 221, 221); border-image: initial; border-radius: 0px;">
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Repo:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">GitHub repository:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">alx-backend-storage</code></li>
                    <li
                    style="box-sizing: border-box;">Directory:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0x00-MySQL_Advanced</code></li>
                        <li
                        style="box-sizing: border-box;">File:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">6-bonus.sql</code></li>
                </ul>
            </div>
        </div>
        <div class="panel-footer" style="box-sizing: border-box; padding: 10px 15px; background-color: rgb(245, 245, 245); border-top: 0px solid rgb(221, 221, 221); border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">
            <div class="align-items-center d-flex justify-content-between" style="box-sizing: border-box; align-items: center !important; display: flex !important; justify-content: space-between !important;">
                <div style="box-sizing: border-box;">
                    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11639" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><span class="no" style="box-sizing: border-box; display: inline;"><i aria-hidden="true" class="fa-regular fa-square " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 400;"></i></span><span> </span>Done
                        <span
                        class="no pending" style="box-sizing: border-box; display: inline;">?</span>
                    </button><span> </span>
                    <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11639" data-batch-id="74" data-toggle="modal" data-target="#task-11639-users-done-modal" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Help</button><span> </span>
                    <button class="btn btn-default btn-sm check-your-task-11639-modal-button" data-task-id="11639" data-toggle="modal" data-target="#task-test-correction-11639-correction-modal" id="task-num-6-check-code-btn"
                    data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11639}" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Check your code</button><span> </span>
                    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11639}"
                    style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><i aria-hidden="true" class="fa-solid fa-terminal " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 900; margin-right: 5px;"></i>
                        <span
                        style="box-sizing: border-box;">Get a sandbox</span>
                    </button>
                </div>
                <div class="fs-4" style="box-sizing: border-box; font-size: 1.5rem !important;"></div>
            </div>
        </div>
    </div>
</div>
<div data-role="task11640" data-position="8" id="task-num-7" style="box-sizing: border-box; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel panel-default task-card " id="task-11640" style="box-sizing: border-box; margin-bottom: 50px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
        <div class="panel-heading panel-heading-actions" style="box-sizing: border-box; padding: 10px 15px; border-bottom: 1px solid rgb(221, 221, 221); border-top-left-radius: 3px; border-top-right-radius: 3px; color: rgb(51, 51, 51); background-color: rgb(245, 245, 245); border-top-color: rgb(221, 221, 221); border-right-color: rgb(221, 221, 221); border-left-color: rgb(221, 221, 221); align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between;">
            <h3 class="panel-title" style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 0px; margin-bottom: 0px; font-size: 16px;">7. Average score</h3>
            <div style="box-sizing: border-box; display: flex;"><span class="label label-info" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 10.5px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(152, 163, 174);">mandatory</span></div>
        </div>
        <div class="panel-body" style="box-sizing: border-box; padding: 15px;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Write a SQL script that creates a stored procedure<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">ComputeAverageScoreForUser</code><span> </span>that
                computes and store the average score for a student. Note: An average score can be a decimal</p>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Requirements:</strong></p>
            <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                <li style="box-sizing: border-box;">Procedure<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">ComputeAverageScoreForUser</code><span> </span>is
                    taking 1 input:
                    <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 0px;">
                        <li style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">user_id</code>,
                            a<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">users.id</code><span> </span>value
                            (you can assume<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">user_id</code><span> </span>is
                            linked to an existing<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">users</code>)</li>
                    </ul>
                </li>
            </ul><pre style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">bob@dylan:~$ cat 7-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    average_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id int not null,
    project_id int not null,
    score int default 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES ("C is fun");
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project_py = LAST_INSERT_ID();


INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$ 
bob@dylan:~$ cat 7-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 7-average_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 7-main.sql
-- Show and compute average score
SELECT * FROM users;
SELECT * FROM corrections;

SELECT "--";
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

SELECT "--";
SELECT * FROM users;

bob@dylan:~$ 
bob@dylan:~$ cat 7-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name    average_score
1   Bob 0
2   Jeanne  0
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name    average_score
1   Bob 0
2   Jeanne  82
bob@dylan:~$ 
</code></pre></div>
        <div class="list-group" style="box-sizing: border-box; padding-left: 0px; margin-bottom: 0px;">
            <div class="list-group-item" style="box-sizing: border-box; position: relative; display: block; padding: 10px 15px; margin-bottom: 0px; background-color: rgb(255, 255, 255); border-width: 1px 0px; border-style: solid; border-color: rgb(221, 221, 221); border-image: initial; border-radius: 0px;">
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Repo:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">GitHub repository:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">alx-backend-storage</code></li>
                    <li
                    style="box-sizing: border-box;">Directory:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0x00-MySQL_Advanced</code></li>
                        <li
                        style="box-sizing: border-box;">File:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">7-average_score.sql</code></li>
                </ul>
            </div>
        </div>
        <div class="panel-footer" style="box-sizing: border-box; padding: 10px 15px; background-color: rgb(245, 245, 245); border-top: 0px solid rgb(221, 221, 221); border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">
            <div class="align-items-center d-flex justify-content-between" style="box-sizing: border-box; align-items: center !important; display: flex !important; justify-content: space-between !important;">
                <div style="box-sizing: border-box;">
                    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11640" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><span class="no" style="box-sizing: border-box; display: inline;"><i aria-hidden="true" class="fa-regular fa-square " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 400;"></i></span><span> </span>Done
                        <span
                        class="no pending" style="box-sizing: border-box; display: inline;">?</span>
                    </button><span> </span>
                    <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11640" data-batch-id="74" data-toggle="modal" data-target="#task-11640-users-done-modal" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Help</button><span> </span>
                    <button class="btn btn-default btn-sm check-your-task-11640-modal-button" data-task-id="11640" data-toggle="modal" data-target="#task-test-correction-11640-correction-modal" id="task-num-7-check-code-btn"
                    data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11640}" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Check your code</button><span> </span>
                    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11640}"
                    style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><i aria-hidden="true" class="fa-solid fa-terminal " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 900; margin-right: 5px;"></i>
                        <span
                        style="box-sizing: border-box;">Get a sandbox</span>
                    </button>
                </div>
                <div class="fs-4" style="box-sizing: border-box; font-size: 1.5rem !important;"></div>
            </div>
        </div>
    </div>
</div>
<div data-role="task11641" data-position="9" id="task-num-8" style="box-sizing: border-box; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel panel-default task-card " id="task-11641" style="box-sizing: border-box; margin-bottom: 50px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
        <div class="panel-heading panel-heading-actions" style="box-sizing: border-box; padding: 10px 15px; border-bottom: 1px solid rgb(221, 221, 221); border-top-left-radius: 3px; border-top-right-radius: 3px; color: rgb(51, 51, 51); background-color: rgb(245, 245, 245); border-top-color: rgb(221, 221, 221); border-right-color: rgb(221, 221, 221); border-left-color: rgb(221, 221, 221); align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between;">
            <h3 class="panel-title" style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 0px; margin-bottom: 0px; font-size: 16px;">8. Optimize simple search</h3>
            <div style="box-sizing: border-box; display: flex;"><span class="label label-info" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 10.5px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(152, 163, 174);">mandatory</span></div>
        </div>
        <div class="panel-body" style="box-sizing: border-box; padding: 15px;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Write a SQL script that creates an index<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">idx_name_first</code><span> </span>on
                the table<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">names</code><span> </span>and
                the first letter of<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">name</code>.</p>
            <p
            style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Requirements:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">Import this table dump:<span> </span><a href="https://intranet.alxswe.com/rltoken/BluyCCIIfw0NqcjqUiUdEw" title="names.sql.zip" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">names.sql.zip</a></li>
                    <li
                    style="box-sizing: border-box;">Only the first letter of<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">name</code><span> </span>must
                        be indexed</li>
                </ul>
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Context:</strong><span> </span><em style="box-sizing: border-box;">Index is not the solution for any performance issue, but well used, it’s really powerful!</em></p><pre style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (2.19 sec)
mysql&gt; 
mysql&gt; exit
bye
bob@dylan:~$ 
bob@dylan:~$ cat 8-index_my_names.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql&gt; SHOW index FROM names;
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name       | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.00 sec)
mysql&gt; 
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (0.82 sec)
mysql&gt; 
mysql&gt; exit
bye
bob@dylan:~$ 
</code></pre></div>
        <div class="list-group" style="box-sizing: border-box; padding-left: 0px; margin-bottom: 0px;">
            <div class="list-group-item" style="box-sizing: border-box; position: relative; display: block; padding: 10px 15px; margin-bottom: 0px; background-color: rgb(255, 255, 255); border-width: 1px 0px; border-style: solid; border-color: rgb(221, 221, 221); border-image: initial; border-radius: 0px;">
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Repo:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">GitHub repository:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">alx-backend-storage</code></li>
                    <li
                    style="box-sizing: border-box;">Directory:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0x00-MySQL_Advanced</code></li>
                        <li
                        style="box-sizing: border-box;">File:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">8-index_my_names.sql</code></li>
                </ul>
            </div>
        </div>
        <div class="panel-footer" style="box-sizing: border-box; padding: 10px 15px; background-color: rgb(245, 245, 245); border-top: 0px solid rgb(221, 221, 221); border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">
            <div class="align-items-center d-flex justify-content-between" style="box-sizing: border-box; align-items: center !important; display: flex !important; justify-content: space-between !important;">
                <div style="box-sizing: border-box;">
                    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11641" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><span class="no" style="box-sizing: border-box; display: inline;"><i aria-hidden="true" class="fa-regular fa-square " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 400;"></i></span><span> </span>Done
                        <span
                        class="no pending" style="box-sizing: border-box; display: inline;">?</span>
                    </button><span> </span>
                    <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11641" data-batch-id="74" data-toggle="modal" data-target="#task-11641-users-done-modal" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Help</button><span> </span>
                    <button class="btn btn-default btn-sm check-your-task-11641-modal-button" data-task-id="11641" data-toggle="modal" data-target="#task-test-correction-11641-correction-modal" id="task-num-8-check-code-btn"
                    data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11641}" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Check your code</button><span> </span>
                    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11641}"
                    style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><i aria-hidden="true" class="fa-solid fa-terminal " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 900; margin-right: 5px;"></i>
                        <span
                        style="box-sizing: border-box;">Get a sandbox</span>
                    </button>
                </div>
                <div class="fs-4" style="box-sizing: border-box; font-size: 1.5rem !important;"></div>
            </div>
        </div>
    </div>
</div>
<div data-role="task11642" data-position="10" id="task-num-9" style="box-sizing: border-box; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel panel-default task-card " id="task-11642" style="box-sizing: border-box; margin-bottom: 50px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
        <div class="panel-heading panel-heading-actions" style="box-sizing: border-box; padding: 10px 15px; border-bottom: 1px solid rgb(221, 221, 221); border-top-left-radius: 3px; border-top-right-radius: 3px; color: rgb(51, 51, 51); background-color: rgb(245, 245, 245); border-top-color: rgb(221, 221, 221); border-right-color: rgb(221, 221, 221); border-left-color: rgb(221, 221, 221); align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between;">
            <h3 class="panel-title" style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 0px; margin-bottom: 0px; font-size: 16px;">9. Optimize search and score</h3>
            <div style="box-sizing: border-box; display: flex;"><span class="label label-info" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 10.5px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(152, 163, 174);">mandatory</span></div>
        </div>
        <div class="panel-body" style="box-sizing: border-box; padding: 15px;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Write a SQL script that creates an index<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">idx_name_first_score</code><span> </span>on
                the table<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">names</code><span> </span>and
                the first letter of<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">name</code><span> </span>and
                the<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">score</code>.</p>
            <p
            style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Requirements:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">Import this table dump:<span> </span><a href="https://intranet.alxswe.com/rltoken/BluyCCIIfw0NqcjqUiUdEw" title="names.sql.zip" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(219, 62, 62); text-decoration: none;">names.sql.zip</a></li>
                    <li
                    style="box-sizing: border-box;">Only the first letter of<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">name</code><span> </span>AND<span> </span>
                        <code
                        style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">score</code><span> </span>must be indexed</li>
                </ul><pre style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score &lt; 80;
+-------------+
| count(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (2.40 sec)
mysql&gt; 
mysql&gt; exit
bye
bob@dylan:~$ 
bob@dylan:~$ cat 9-index_name_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql&gt; SHOW index FROM names;
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name             | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first_score |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
| names |          1 | idx_name_first_score |            2 | score       | A         |        3901 |     NULL | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set (0.00 sec)
mysql&gt; 
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score &lt; 80;
+-------------+
| COUNT(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (0.48 sec)
mysql&gt; 
mysql&gt; exit
bye
bob@dylan:~$ 
</code></pre></div>
        <div class="list-group" style="box-sizing: border-box; padding-left: 0px; margin-bottom: 0px;">
            <div class="list-group-item" style="box-sizing: border-box; position: relative; display: block; padding: 10px 15px; margin-bottom: 0px; background-color: rgb(255, 255, 255); border-width: 1px 0px; border-style: solid; border-color: rgb(221, 221, 221); border-image: initial; border-radius: 0px;">
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Repo:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">GitHub repository:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">alx-backend-storage</code></li>
                    <li
                    style="box-sizing: border-box;">Directory:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0x00-MySQL_Advanced</code></li>
                        <li
                        style="box-sizing: border-box;">File:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">9-index_name_score.sql</code></li>
                </ul>
            </div>
        </div>
        <div class="panel-footer" style="box-sizing: border-box; padding: 10px 15px; background-color: rgb(245, 245, 245); border-top: 0px solid rgb(221, 221, 221); border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">
            <div class="align-items-center d-flex justify-content-between" style="box-sizing: border-box; align-items: center !important; display: flex !important; justify-content: space-between !important;">
                <div style="box-sizing: border-box;">
                    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11642" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><span class="no" style="box-sizing: border-box; display: inline;"><i aria-hidden="true" class="fa-regular fa-square " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 400;"></i></span><span> </span>Done
                        <span
                        class="no pending" style="box-sizing: border-box; display: inline;">?</span>
                    </button><span> </span>
                    <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11642" data-batch-id="74" data-toggle="modal" data-target="#task-11642-users-done-modal" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Help</button><span> </span>
                    <button class="btn btn-default btn-sm check-your-task-11642-modal-button" data-task-id="11642" data-toggle="modal" data-target="#task-test-correction-11642-correction-modal" id="task-num-9-check-code-btn"
                    data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11642}" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Check your code</button><span> </span>
                    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11642}"
                    style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><i aria-hidden="true" class="fa-solid fa-terminal " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 900; margin-right: 5px;"></i>
                        <span
                        style="box-sizing: border-box;">Get a sandbox</span>
                    </button>
                </div>
                <div class="fs-4" style="box-sizing: border-box; font-size: 1.5rem !important;"></div>
            </div>
        </div>
    </div>
</div>
<div data-role="task11643" data-position="11" id="task-num-10" style="box-sizing: border-box; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel panel-default task-card " id="task-11643" style="box-sizing: border-box; margin-bottom: 50px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
        <div class="panel-heading panel-heading-actions" style="box-sizing: border-box; padding: 10px 15px; border-bottom: 1px solid rgb(221, 221, 221); border-top-left-radius: 3px; border-top-right-radius: 3px; color: rgb(51, 51, 51); background-color: rgb(245, 245, 245); border-top-color: rgb(221, 221, 221); border-right-color: rgb(221, 221, 221); border-left-color: rgb(221, 221, 221); align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between;">
            <h3 class="panel-title" style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 0px; margin-bottom: 0px; font-size: 16px;">10. Safe divide</h3>
            <div style="box-sizing: border-box; display: flex;"><span class="label label-info" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 10.5px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(152, 163, 174);">mandatory</span></div>
        </div>
        <div class="panel-body" style="box-sizing: border-box; padding: 15px;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Write a SQL script that creates a function<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">SafeDiv</code><span> </span>that
                divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.</p>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Requirements:</strong></p>
            <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                <li style="box-sizing: border-box;">You must create a function</li>
                <li style="box-sizing: border-box;">The function<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">SafeDiv</code><span> </span>takes
                    2 arguments:
                    <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 0px;">
                        <li style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">a</code>,
                            INT</li>
                        <li style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">b</code>,
                            INT</li>
                    </ul>
                </li>
                <li style="box-sizing: border-box;">And returns<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">a / b</code><span> </span>or
                    0 if<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">b == 0</code></li>
            </ul><pre style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">bob@dylan:~$ cat 10-init.sql
-- Initial
DROP TABLE IF EXISTS numbers;

CREATE TABLE IF NOT EXISTS numbers (
    a int default 0,
    b int default 0
);

INSERT INTO numbers (a, b) VALUES (10, 2);
INSERT INTO numbers (a, b) VALUES (4, 5);
INSERT INTO numbers (a, b) VALUES (2, 3);
INSERT INTO numbers (a, b) VALUES (6, 3);
INSERT INTO numbers (a, b) VALUES (7, 0);
INSERT INTO numbers (a, b) VALUES (6, 8);

bob@dylan:~$ cat 10-init.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 10-div.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT (a / b) FROM numbers;" | mysql -uroot -p holberton
Enter password: 
(a / b)
5.0000
0.8000
0.6667
2.0000
NULL
0.7500
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT SafeDiv(a, b) FROM numbers;" | mysql -uroot -p holberton
Enter password: 
SafeDiv(a, b)
5
0.800000011920929
0.6666666865348816
2
0
0.75
bob@dylan:~$ 
</code></pre></div>
        <div class="list-group" style="box-sizing: border-box; padding-left: 0px; margin-bottom: 0px;">
            <div class="list-group-item" style="box-sizing: border-box; position: relative; display: block; padding: 10px 15px; margin-bottom: 0px; background-color: rgb(255, 255, 255); border-width: 1px 0px; border-style: solid; border-color: rgb(221, 221, 221); border-image: initial; border-radius: 0px;">
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Repo:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">GitHub repository:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">alx-backend-storage</code></li>
                    <li
                    style="box-sizing: border-box;">Directory:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0x00-MySQL_Advanced</code></li>
                        <li
                        style="box-sizing: border-box;">File:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">10-div.sql</code></li>
                </ul>
            </div>
        </div>
        <div class="panel-footer" style="box-sizing: border-box; padding: 10px 15px; background-color: rgb(245, 245, 245); border-top: 0px solid rgb(221, 221, 221); border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">
            <div class="align-items-center d-flex justify-content-between" style="box-sizing: border-box; align-items: center !important; display: flex !important; justify-content: space-between !important;">
                <div style="box-sizing: border-box;">
                    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11643" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><span class="no" style="box-sizing: border-box; display: inline;"><i aria-hidden="true" class="fa-regular fa-square " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 400;"></i></span><span> </span>Done
                        <span
                        class="no pending" style="box-sizing: border-box; display: inline;">?</span>
                    </button><span> </span>
                    <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11643" data-batch-id="74" data-toggle="modal" data-target="#task-11643-users-done-modal" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Help</button><span> </span>
                    <button class="btn btn-default btn-sm check-your-task-11643-modal-button" data-task-id="11643" data-toggle="modal" data-target="#task-test-correction-11643-correction-modal" id="task-num-10-check-code-btn"
                    data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11643}" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Check your code</button><span> </span>
                    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11643}"
                    style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><i aria-hidden="true" class="fa-solid fa-terminal " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 900; margin-right: 5px;"></i>
                        <span
                        style="box-sizing: border-box;">Get a sandbox</span>
                    </button>
                </div>
                <div class="fs-4" style="box-sizing: border-box; font-size: 1.5rem !important;"></div>
            </div>
        </div>
    </div>
</div>
<div data-role="task11644" data-position="12" id="task-num-11" style="box-sizing: border-box; color: rgb(51, 51, 51); font-family: aktiv-grotesk, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="panel panel-default task-card " id="task-11644" style="box-sizing: border-box; margin-bottom: 50px; background-color: rgb(255, 255, 255); border: 1px solid rgb(221, 221, 221); border-radius: 4px; box-shadow: none; overflow: hidden;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
        <div class="panel-heading panel-heading-actions" style="box-sizing: border-box; padding: 10px 15px; border-bottom: 1px solid rgb(221, 221, 221); border-top-left-radius: 3px; border-top-right-radius: 3px; color: rgb(51, 51, 51); background-color: rgb(245, 245, 245); border-top-color: rgb(221, 221, 221); border-right-color: rgb(221, 221, 221); border-left-color: rgb(221, 221, 221); align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between;">
            <h3 class="panel-title" style="box-sizing: border-box; font-family: inherit; font-weight: 500; line-height: 1.1; color: rgb(51, 51, 51); margin-top: 0px; margin-bottom: 0px; font-size: 16px;">11. No table for a meeting</h3>
            <div style="box-sizing: border-box; display: flex;"><span class="label label-info" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 10.5px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(152, 163, 174);">mandatory</span></div>
        </div>
        <div class="panel-body" style="box-sizing: border-box; padding: 15px;"><span id="user_id" data-id="229284" style="box-sizing: border-box;"></span>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;">Write a SQL script that creates a view<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">need_meeting</code><span> </span>that
                lists all students that have a score under 80 (strict) and no<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">last_meeting</code><span> </span>or
                more than 1 month.</p>
            <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Requirements:</strong></p>
            <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                <li style="box-sizing: border-box;">The view<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">need_meeting</code><span> </span>should
                    return all students name when:
                    <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 0px;">
                        <li style="box-sizing: border-box;">They score are under (strict) to 80</li>
                        <li style="box-sizing: border-box;"><strong style="box-sizing: border-box; font-weight: bold;">AND</strong><span> </span>no<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">last_meeting</code><span> </span>date<span> </span>
                            <strong
                            style="box-sizing: border-box; font-weight: bold;">OR</strong><span> </span>more than a month</li>
                    </ul>
                </li>
            </ul><pre style="box-sizing: border-box; overflow: auto; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 13px; display: block; padding: 9.5px; margin: 0px 0px 10px; line-height: 1.42857; color: rgb(51, 51, 51); word-break: break-all; overflow-wrap: break-word; background-color: rgb(245, 245, 245); border: 1px solid rgb(204, 204, 204); border-radius: 4px;"><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: inherit; padding: 0px; color: inherit; background-color: transparent; border-radius: 0px; white-space: pre-wrap;">bob@dylan:~$ cat 11-init.sql
-- Initial
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT default 0,
    last_meeting DATE NULL 
);

INSERT INTO students (name, score) VALUES ("Bob", 80);
INSERT INTO students (name, score) VALUES ("Sylvia", 120);
INSERT INTO students (name, score) VALUES ("Jean", 60);
INSERT INTO students (name, score) VALUES ("Steeve", 50);
INSERT INTO students (name, score) VALUES ("Camilia", 80);
INSERT INTO students (name, score) VALUES ("Alexa", 130);

bob@dylan:~$ cat 11-init.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 11-need_meeting.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 11-main.sql
-- Test view
SELECT * FROM need_meeting;

SELECT "--";

UPDATE students SET score = 40 WHERE name = 'Bob';
SELECT * FROM need_meeting;

SELECT "--";

UPDATE students SET score = 80 WHERE name = 'Steeve';
SELECT * FROM need_meeting;

SELECT "--";

UPDATE students SET last_meeting = CURDATE() WHERE name = 'Jean';
SELECT * FROM need_meeting;

SELECT "--";

UPDATE students SET last_meeting = ADDDATE(CURDATE(), INTERVAL -2 MONTH) WHERE name = 'Jean';
SELECT * FROM need_meeting;

SELECT "--";

SHOW CREATE TABLE need_meeting;

SELECT "--";

SHOW CREATE TABLE students;

bob@dylan:~$ 
bob@dylan:~$ cat 11-main.sql | mysql -uroot -p holberton
Enter password: 
name
Jean
Steeve
--
--
name
Bob
Jean
Steeve
--
--
name
Bob
Jean
--
--
name
Bob
--
--
name
Bob
Jean
--
--
View    Create View character_set_client    collation_connection
XXXXXX&lt;yes, here it will display the View SQL statement :-) &gt;XXXXXX
--
--
Table   Create Table
students    CREATE TABLE `students` (\n  `name` varchar(255) NOT NULL,\n  `score` int(11) DEFAULT '0',\n  `last_meeting` date DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
bob@dylan:~$ 
</code></pre></div>
        <div class="list-group" style="box-sizing: border-box; padding-left: 0px; margin-bottom: 0px;">
            <div class="list-group-item" style="box-sizing: border-box; position: relative; display: block; padding: 10px 15px; margin-bottom: 0px; background-color: rgb(255, 255, 255); border-width: 1px 0px; border-style: solid; border-color: rgb(221, 221, 221); border-image: initial; border-radius: 0px;">
                <p style="box-sizing: border-box; margin: 0px 0px 10px;"><strong style="box-sizing: border-box; font-weight: bold;">Repo:</strong></p>
                <ul style="box-sizing: border-box; margin-top: 0px; margin-bottom: 10px;">
                    <li style="box-sizing: border-box;">GitHub repository:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">alx-backend-storage</code></li>
                    <li
                    style="box-sizing: border-box;">Directory:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">0x00-MySQL_Advanced</code></li>
                        <li
                        style="box-sizing: border-box;">File:<span> </span><code style="box-sizing: border-box; font-family: Menlo, Monaco, Consolas, &quot;Courier New&quot;, monospace; font-size: 12.6px; padding: 2px 4px; color: rgb(199, 37, 78); background-color: rgb(249, 242, 244); border-radius: 4px;">11-need_meeting.sql</code></li>
                </ul>
            </div>
        </div>
        <div class="panel-footer" style="box-sizing: border-box; padding: 10px 15px; background-color: rgb(245, 245, 245); border-top: 0px solid rgb(221, 221, 221); border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;">
            <div class="align-items-center d-flex justify-content-between" style="box-sizing: border-box; align-items: center !important; display: flex !important; justify-content: space-between !important;">
                <div style="box-sizing: border-box;">
                    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11644" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);"><span class="no" style="box-sizing: border-box; display: inline;"><i aria-hidden="true" class="fa-regular fa-square " style="box-sizing: border-box; -webkit-font-smoothing: antialiased; display: var(--fa-display, inline-block); font-style: normal; font-variant: normal; line-height: 1; text-rendering: auto; font-family: &quot;Font Awesome 6 Free&quot;; font-weight: 400;"></i></span><span> </span>Done
                        <span
                        class="no pending" style="box-sizing: border-box; display: inline;">?</span>
                    </button><span> </span>
                    <button class="student-task-done-by btn btn-default btn-sm" data-task-id="11644" data-batch-id="74" data-toggle="modal" data-target="#task-11644-users-done-modal" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Help</button><span> </span>
                    <button class="btn btn-default btn-sm check-your-task-11644-modal-button" data-task-id="11644" data-toggle="modal" data-target="#task-test-correction-11644-correction-modal" id="task-num-11-check-code-btn"
                    data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11644}" style="box-sizing: border-box; color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: normal; font-stretch: inherit; font-size: 12px; line-height: 1.5; font-family: inherit; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; overflow: visible; text-transform: none; appearance: button; cursor: pointer; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; touch-action: manipulation; background-image: none; border: 1px solid rgb(204, 204, 204); padding: 5px 10px; border-radius: 3px; user-select: none; background-color: rgb(255, 255, 255);">Check your code</button><span> </span></div>
            </div>
        </div>
    </div>
</div>