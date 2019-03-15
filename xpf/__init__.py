"""
#Overview
Xpf is an interface to perforce which offers the following benefits:

    * Pure python, no compiled dependencies (allow for use in Python 2, Python 3, Max, Maya & Motion Builder etc)
    * Failsafe calls - this module will not raise errors if the perforce server is in-accessible.
    * PyPi distribution making it easier for sharing tools with outsourcers
    * Easy form injection


#Why not P4Python

Perforce offers its own p4Python module which is a well established and
stable library.

The downside to P4Python is that its a compiled library and therefore requires
different distributions if you're jumping between Python 2.x and Python 3.x

This is further exasperated when wanting to utilise perforce integrations into
tools built within embedded interpreters such as Autodesk Maya/Max/Motionbuilder
which are all compiled against different compiler versions than the native
python distributions.

The other benefit xpf brings is that its has a soft requirement on perforce.
Its common place to want to embed perforce support into tools within
applications such as Max/Maya but it opens the challenge of allowing your tools
to still operate outside of your studio environments when the Perforce server
is in-accessible.

Xpf resolves this by ensuring all the perforce calls can return default
variable types in circumstances where the Perforce server is unreachable. This
allows for tools to operate outside the main studio environment, and is made
easier by xpf being freely accessible on PyPi.


##Xpf Direct
The library tries to make it easy to use for those that are used to utilising
P4Python or the perforce command line. With that in mind you can utilise the
the ```xpf.direct``` module which mimics the types of calls and interface of
P4Python.

In this regard you're given access to functions for each perforce command and
are able to pass in any arguments you want to give. As per P4Python conventions
you will be returned a list of dictionaries representing the results.

Some examples of this would be:

```python
import xpf

# -- Sync to the head revision of a directory
xpf.direct.sync(
    [
        '/usr/my_files/...'
    ]
)

# -- Force sync, passing the usual perforce argument switches
xpf.direct.sync(
    [
        '/usr/my_files/...'
    ],
    '-f',
)
```

As well as the defined functions (which are auto-generated) there is also a
more generic run function which you can utilise directly:

```python
import xpf

# -- Sync to the head revision of a directory
result = xpf.direct.run(
    'describe',
    13569,                  # -- Change list to describe
    'Os',                   # -- Shorten output by excluding client workspace data
    'Rc',                   # -- Limit output to files mapped into the current workspace.
)
```

Using ```xpf.direct``` should feel very familiar to anyone who has utilised
P4Python or the perforce commandline.


##Xpf Assist
Working at the ```xpf.direct``` level makes a lot of sense in a lot of
situations, however there are various circumstances which call for multiple
queries to be carried out in order to answer slightly higher level questions.

Examples of these might be to add a file to a changelist regardless of whether
its an add or edit operation. Another example might be where you want to manage
the changelist descriptions a little easier.

The ```xpf.assist``` module aims to give higher level functionality whereby the
function in question will carry out multiple calls and wrangle data to solve
a particular request.

Examples of these are:

```python
import xpf

# -- Given a chnagelist description, find the most likely changelist
# -- number for the current user. In this case, if that changelist
# -- does not exist it will be created for you
result = xpf.assist.get_changelist('My change description')
```

The following example exposes a method of submitting which forces all
files being submitted to be added to a changelist with the supplied
description and submitted together:

```python
import xpf

xpf.assist.submit_files(
    [
        '/usr/my_files/...'
    ],
    description='My submission description',
)
```


##Xpf Variables

Xpf works at a module level. It is not class based and it wraps the perforce
command line. With this in mind it has some variables which are considered
global, which are queried for on the first run (based on p4 set) but can be
altered by you.

```python
import xpf

# -- Get the host
host = xpf.variables.get_host()

# -- Set the host to something specific
xpf.variables.set_host(host)
```

Variables which can be retrieved and set in this way include:

    * host
    * client
    * user
    * port (server)
    * timeout

A special variable which can be turned on/off is the `debugging` variable.
When debugging is turned on xpf will print ever command line its about to
process in the final format its constructed in. This is particularly useful
if you're getting a result you do not expect and want to recreate the steps
using the commandline.

To enable this option you do:

```python
import xpf

xpf.variables.set_debug(True)
```
##Failsafes

One of the big advantages of xpf is that includes in-built failsafe mechanisms
to protect functionality whenever the server is in-accessible. During the first
xpf call (regardless of whether that is through ```xpf.direct``` or
```xpf.assist```) a ```p4 info``` query is run. If this timesout then the
xpf variable is set to mark the server as inaccessible.

When a server is inaccessible all functions will return a default value which
is defined by their failsafe decorator. This allows your code to continue
without having to handle server failure directly.

In many situations when calling functions within ```xpf.direct``` they will
return an empty list upon server failure - this is because their functions
usually return a list. With that in mind, whilst you dont have to handle server
failure you should handle being given empty data of the correct (expected)
type.

A good example of this would be:

```python

description = xpf.direct.describe(13569)

if not description:
    pass

...
```

In the example above we do have to handle not being given a description but
we do not have to handle unexpected exceptions beacuse of an inaccessible
perforce server.

Fundamentally this means you can safely embed an xpf dependency in your tool
to give a rich user experience knowing that the tool will work even if its taken
off-site.


##Timeouts

Xpf offers the ability to define a timeout on all perforce queries. By default
this timeout is exposed through ```xpf.set_timeout(value)``` and is defaulted
to one second. If your server is particularly slow you can use that call to
increase the global timeout.

Alternatively, you can set the timeout on a per-call basis too. This is
particularly useful when you know your call will take a longer than expected
time. This is done with the `timeout` argument as shown here:

```python
import xpf

xpf.direct.info(timeout=10)
```


## Marshalling

By default all queries run through xpf are marshaled, and therefore return
pythonic objects. If you want raw output (strings) rather than lists of
dictionaries you can set the marshaling to false on a per call basis as
shown here:

```python
string_dump = xof.direct.run('set', marshal=False)  # -- (Equivalent to p4 set)
```

##Forms

Forms are used in perforce to deliver multiple pieces of user input. When
running perforce through the commandline this typically pops open a text
editor - which is not particularly useful when interacting with perforce
via a python library.

Therefore all forms that are requested by a particular p4 command can be
given in the form of a dictionary. This is shown here:

```python
import xpf

result = xpf.direct.changelist(
    '-i',
    form={
        'Change': 'new',
        'Status': 'new',
        'Description': 'My New Changelist Description',
    },
    **kwargs
)
```


#Compatibility

Xpf has been tested under Python 2.7 and Python 3.7 on Windows.
"""
from . import assist
from . import direct
from . import variables
from . import connection
