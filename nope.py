import sys


def parse(ll):
	parencounter = ""
	tablevel = 0
	end = []
	for l in ll:
		if l[0] == "\t":
			end.append(l[0] + "(" + l[1:])
			parencounter = parencounter + ")"
		elif l[0] == "\n":
			# it would be nice to just append the close parens to the end of previous line, but maybe that's an after-the-fact task
			# close all open parens
			# make it parse like python and not depend on counting linebreaks, instead store tab level?
			# tab level is just number of parens...
			# actually need tab level for 
			# but the only time we should have same tab level is when there are side effects like in a 
			# dosync kind of thing... 
			# consequence of this is it won't allow implicit line continuations...





if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		lines = f.readlines()
		parse(lines)