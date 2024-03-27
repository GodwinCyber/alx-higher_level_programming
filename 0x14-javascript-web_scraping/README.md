<h1><strong>0x14. JavaScript - Web scraping</strong></h1>
<div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[{&quot;id&quot;:28,&quot;value&quot;:&quot;Scripting&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:36,&quot;value&quot;:&quot;API&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:46,&quot;value&quot;:&quot;JavaScript&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;}]}" data-react-cache-id="tags/Tags-0"></div>
<div data-react-class="projects/ProjectMetadata" data-react-props="{&quot;metadata&quot;:{&quot;weight&quot;:1,&quot;correction&quot;:{&quot;released&quot;:true,&quot;requires_auto_correction&quot;:true,&quot;requires_manual_correction&quot;:false},&quot;bpi&quot;:{&quot;current&quot;:false,&quot;in_second_deadline&quot;:true,&quot;starts_at&quot;:&quot;2024-03-26T06:00:00.000+01:00&quot;,&quot;ends_at&quot;:&quot;2024-03-27T06:00:00.000+01:00&quot;,&quot;second_deadline_at&quot;:&quot;2024-03-28T06:00:00.000+01:00&quot;}}}" data-react-cache-id="projects/ProjectMetadata-0"></div>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/ONv-sSv-FA87Mc5rMZmO6A" title="Working with JSON data" target="_blank">Working with JSON data</a> </li>
<li><a href="/rltoken/zm0h7FqpQCZZpPZqxxwLxA" title="The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco" target="_blank">The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco</a> </li>
<li><a href="/rltoken/goymbxGy-cTc5ZdKBTUcTQ" title="request module" target="_blank">request module</a> </li>
<li><a href="/rltoken/j2PStAUtVPdXKwrrFxpt0g" title="Modern JS" target="_blank">Modern JS</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/yZIL5HK-2hHAP-RJF6yInQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why JavaScript programming is amazing</li>
<li>How to manipulate JSON data</li>
<li>How to use <code>request</code> and fetch API</li>
<li>How to read and write a file using <code>fs</code> module</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS using <code>node</code> (version 14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/node</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be <code>semistandard</code> compliant. <a href="/rltoken/W9rASrTqkF-xXjcwomrMLw" title="Rules of Standard" target="_blank">Rules of Standard</a> + <a href="/rltoken/GXh9DyGGivUB7pdq9Oqmzg" title="semicolons on top" target="_blank">semicolons on top</a>. Also as reference: <a href="/rltoken/NZR55f9vk1dZXj5q7UI5mQ" title="AirBnB style" target="_blank">AirBnB style</a></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<h2>More Info</h2>

<h3>Install Node 14</h3>

<pre><code>$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>

<h3>Install semi-standard</h3>

<p><a href="/rltoken/GXh9DyGGivUB7pdq9Oqmzg" title="Documentation" target="_blank">Documentation</a></p>

<pre><code>$ sudo npm install semistandard --global
</code></pre>

<h3>Install <code>request</code> module and use it</h3>

<p><a href="/rltoken/goymbxGy-cTc5ZdKBTUcTQ" title="Documentation" target="_blank">Documentation</a></p>

<pre><code>$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
</code></pre>

<p><strong>Notes:</strong> Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it&rsquo;s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).</p>
