#!/usr/bin/env python
import os
import sys
import importlib
try:
    import settings
except ImportError:
    print >>sys.stderr, "Do: cp settings.py.sample setting.py; vim settings.py"
    sys.exit(1)


def global_settings():
    return {'PLATFORM': settings.PLATFORM}

def link(recipe, src, dest):
    abs_src = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'recipes', recipe, src)
    abs_dest = os.path.expanduser(dest)
    try:
        os.symlink(abs_src, abs_dest)
    except:
        print >>sys.stderr, "Trouble linking %s to %s." % (abs_src, abs_dest)
    else:
        print "Linked %s to %s." % (abs_src, abs_dest)

def touch(dest):
    path = os.path.expanduser(dest)
    try:
        open(path, 'w').close()
    except:
        print >>sys.stderr, "Trouble creating empty file %s." % path
    else:
        print "Created empty file %s." % path

def main():
    for args in settings.REGISTER_CONFIGS:
        options = global_settings()
        if isinstance(args, basestring):
            recipe = args
        elif len(args) == 1:
            recipe = args[0]
        else:
            recipe, recipe_opts = args
            options.update(recipe_opts)
        module = importlib.import_module("recipes.%s" % recipe)
        if hasattr(module, 'FILES_TO_LINK'):
            for src, dest in (module.FILES_TO_LINK.get(settings.PLATFORM, ()) +
                              module.FILES_TO_LINK.get('any', ())):
                link(recipe, src, dest)
        if hasattr(module, 'EMPTY_FILES'):
            for dest in (module.EMPTY_FILES.get(settings.PLATFORM, ()) +
                         module.EMPTY_FILES.get('any', ())):
                touch(dest)
        if hasattr(module, 'install'):
            module.install(**options)


if __name__ == '__main__':
    print "Make sure you have git and zsh installed."
    raw_input("Press enter.. ")
    main()
