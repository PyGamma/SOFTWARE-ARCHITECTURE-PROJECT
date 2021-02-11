
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

"""
@Core contributer: Gama Richard Williams
"""

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'School system.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
"""
As per the standard convention of  software development, its a good idea 
the project name to be in lowercase(). Well we often embrace the software 
 development ethics.
This reminds me my early college course "Software Engineering Ethics". 

"""

"""
Here is the usecase:  Insteading of writing <title>SOFTWARE-ARCHITECTURE-PROJECT>/title>, 
its a good coding practice to write it as <title>software-architecture-project</title>
"""
"""
Hey am a newbie in python , hope have  documented my commment as per the 
language standards
"""

if __name__ == '__main__':
    main()

