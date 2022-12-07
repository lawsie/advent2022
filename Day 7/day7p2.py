with open("input.txt") as f:
    shell = [s.strip("\n") for s in f.readlines()]

class Directory:
    def __init__(self, dirname, parentdir = "/", is_root=False):
        self.name = dirname
        self.parent = parentdir
        self.is_root = is_root
        self.subdirectories = []
        self.files = []
    
    
    def find_child(self, dirname):
        for sd in self.subdirectories:
            if sd.name == dirname:
                return sd
        return None

    def add_subdirectory(self, subdirname):
        self.subdirectories.append(Directory(subdirname, parentdir=self))
    
    def add_file(self,filename, filesize):
        self.files.append(File(filename, filesize))
    
    def change_to(self, dirname):
        target = self.child_names().index(dirname) # Find the index of the directory we need
        if target is not None:            
            return self.subdirectories[target]
        
    def child_names(self):
        dirnames = []
        for dir in self.subdirectories:
            dirnames.append(dir.name)
        return dirnames
    
    def file_names(self):
        return[f.name for f in filenames]
    
    def total_size(self):
        return sum([f.size for f in self.files])


class File:
    def __init__(self, filename, filesize):
        self.name = filename
        self.size = int(filesize)


class ShellLine:
    def __init__(self, line_text):
        self.contents = line_text.split(" ")

        self.is_command = True if self.contents[0] == "$" else False
        self.command = self.contents[1] if self.contents[0] == "$" else None
        self.changeto = self.contents[2] if self.is_command and self.contents[1] == "cd" else None
        
        self.is_file = True if self.contents[0] not in ["$", "dir"] else False
        self.filesize = self.contents[0] if self.is_file else None
        self.filename = self.contents[1] if self.is_file else None
        
        self.is_dir = True if self.contents[0] == "dir" else False
        self.dirname = self.contents[1] if self.is_dir else None
        
def traverse(node):

    # Output the data of the current node
    print("Traversing", node.name)
    size = 0

    # If there are any subdirectories, traverse those too
    if len(node.subdirectories) > 0:
        for sub in node.subdirectories:
            size += traverse(sub)

    # Get the files that are in the current directory
    size += node.total_size()

    print("Node", node.name, "total size", size)

    return size

def find_target_dir(node, space_needed):

    # Output the data of the current node
    print("Traversing", node.name)
    size = 0

    # If there are any subdirectories, traverse those too
    if len(node.subdirectories) > 0:
        for sub in node.subdirectories:
            size += find_target_dir(sub, space_needed)

    # Get the files that are in the current directory
    size += node.total_size()

    print("Node", node.name, "total size", size)

    if size >= space_needed:
        global found
        if size < found or found == 0:
            found = size

    return size
    

if __name__ == "__main__":
    # Create a root directory
    root = Directory("/", parentdir=None, is_root=True)
    current = root

    # Create an object for each line in the shell
    shellobjects = [ShellLine(s) for s in shell]

    # Loop through and create a directory structure
    for s in shellobjects:
        if s.is_command: # If the instruction was a command
            if s.command == "cd": # Change directory
                match s.changeto:
                    case "..":                
                        if current.parent is not None:
                            current = current.parent
                    case "/":
                        current = root
                    case _:
                        current = current.change_to(s.changeto)
                         
                            
        elif s.is_dir and s.dirname not in current.child_names():
            current.add_subdirectory(s.dirname)

        elif s.is_file and s.filename not in current.files:
            current.add_file(s.filename, s.filesize)
    

    # Some constants 
    TOTAL_DISK_SPACE = 70000000
    UNUSED_SPACE_REQUIRED = 30000000

    # Find out how much space is needed
    free_space = TOTAL_DISK_SPACE - traverse(root)
    target = UNUSED_SPACE_REQUIRED - free_space

    found = 0
    find_target_dir(root, target)
    print(found)

    


