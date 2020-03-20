import os, sys
from os.path import join, dirname
from dotenv import load_dotenv

class env:
    def __init__(self, env_file='.env'):
        self.params = []
        self.file = env_file
        self.is_loaded = False
        #If file exist then load it
        if self.exists():
            self.load()
            self.is_loaded = True

    #If default value is None, then param is required. If default value is present then is optional
    def add_param(self, name, value = None):
        #check if param exists already
        indices = [index for index, param in enumerate(self.params) if param['name'] == name]
        if len(indices) == 0: 
            self.params.append({"name":name, "value": value})
        else:
            #If exist and default value not none, then replace the value of existing param
            #print("Error: The param already exist")
            index = indices[0]
            if value is not None:
                self.params[index]["value"] = value 
    def exists(self):
        if not os.path.isfile(self.file):
            return False
        else:
            return True
    def create(self):
        error = False
        try:
            env = open(self.file, "a")
            print("Creating your {} file\n".format(self.file))
            for index, param in enumerate(self.params):
                option = input(param["name"] + (" ( " + param["value"] + " )" if param["value"] is not None else "") + " : ")
                if param["value"] is None and option == '':
                    raise Exception("invalid value to param")
                elif option == '':
                    option = param["value"]
                env.write("{2}{0}=\"{1}\"".format(param["name"], option, "\n" if index != 0 else ""))
        except OSError:
            print ("Could not open/read file: ", self.file)
            error = True
        except IOError:
            print("An error ocurred trying to write file: ", self.file)
            error = True
        except:
            print("Error: Env param required.")
            error = True
        finally:
            env.close()
            if error:
                os.remove(self.file)
                sys.exit()
    def update(self):
        #Clean file content
        open(self.file,"w").close()
        #recreate file content
        error = False
        try:
            env = open(self.file, "a")
            print("Updating {} file\n".format(self.file))
            for index, param in enumerate(self.params):
                if param["value"] is None:
                    raise Exception("invalid value to param")
                else:
                    env.write("{2}{0}=\"{1}\"".format(param["name"], param["value"], "\n" if index != 0 else ""))
        except OSError:
            print ("Could not open/read file: ", self.file)
            error = True
        except IOError:
            print("An error ocurred trying to write file: ", self.file)
            error = True
        except:
            print("Error: Env param required.")
            error = True
        finally:
            env.close()
            if error:
                sys.exit()
            else:
                #Load the file
                self.load()
    def load(self):
        #Load environment
        envpath = join(dirname(__file__),"./"+self.file)
        load_dotenv(envpath)
        #Get the current values - Usefull for update process
        try:
            env_lines = open(self.file, "r")
            for line in env_lines:
                clean_line = line.replace('"','')
                if len(clean_line.split("=")) == 2:
                    (name,value) = list(clean_line.split("="))
                    self.add_param(name=name, value=value)
        except:
            print("There was an error trying to extract the "+self.file+" values")
        finally:
            env_lines.close()
    def set_param(self, name, value):
        self.add_param(name, value)
    def get(self, name):
        return self.params[name]
    def get_env_vars(self, reload = False):
        if not self.is_loaded or reload:
            os.environ.clear()
            self.load()
        return os.environ