from src.utils.exception import debug, Exception, ExceptionLevel

def formatArgs(args: list) -> dict:
	"""
	Format the command line arguments into a list of key-value pairs.

	Args:
		args (list): A list of command line arguments.
	
	Returns:
		dict: A dictionary of key-value pairs representing the formatted arguments.
	"""
	formatted_args: dict = {}
	accepted_args_flags: list = ["--driver2", "--year", "--round", "--session", "--output", "--export"]

	formatted_args["driver1"] = args[0]
	for flag in accepted_args_flags:
		if flag in args: # check if the flag is present in the args list
			index: int = args.index(flag)
			if index + 1 < len(args):
				formatted_args[flag[2:]] = args[index + 1] # get the value of the flag and add it to the formatted_args dictionary
			else:
				debug.log(Exception(f"Missing value for argument {flag}", ExceptionLevel.TERMINATE))