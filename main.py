import sys 

def main():
    if len(sys.argv)==1:
        return """
        Error : Insufficient Arguments given ,
            use one of these commands : 
            add <description> : to add new task 
            delete <id>  : to delete a task 
            update <id> : to update task 
            list : to list all tasks 
            list <todo|in-progress|done> : to see status wise task list 
            mark <todo|in-progress|done> <id> : to update status of task 
        """
    cli_args = sys.argv[1:]
    cmd = cli_args[0]
    match cmd:
        case "add":
            # create Task object here , store it using storage object 
            pass 
        case "delete":
            # find task object in storage object and delete it 
            pass 
        case "update":
            # update task object with given
            pass 
        case "list":
            #list all objects from storage 
            pass 
        case "mark":
            #mark task in storage 
            pass 
        case _:
            return """ Error : Invalid command """
if __name__ == "__main__":
    print(main())