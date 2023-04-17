"""
System Security
---------------
    1. Permissions Settings
    2. User Registration / Signup
    3. Granting Permissions
    4. Authentication
    5. Authorization

Authentication: is the process of ascertaining that somebody really is who they claim to be.
Authorization: refers to rules that determine who is allowed to do what. E.g. Adam may be authorized to create and delete databases, while Usama is only authorised to read.

The two concepts are completely orthogonal and independent, but both are central to security design, and the failure to get either one correct opens up the avenue to compromise.

In terms of web apps, very crudely speaking, 
Authentication: is when you check login credentials to see if you recognize a user as logged in, 
and 
Authorization: is when you look up in your access control whether you allow the user to view, edit, delete or create content.
"""