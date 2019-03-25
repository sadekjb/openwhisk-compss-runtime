from pycompss.api.task import task
from pycompss.api.parameter import FILE_INOUT

@task(filePath = FILE_INOUT)
def increment(filePath):
    # Read value
    fis = open(filePath, 'r')
    value = fis.read()
    fis.close()
    # Write value
    fos = open(filePath, 'w')
    fos.write(str(int(value) + 1))
    fos.write('\n')
    fos.close()

def main_program():
    from pycompss.api.api import compss_open
    # Check and get parameters
#    if len(sys.argv) != 2:
#        exit(-1)
    initialValue = sys.argv[1]
    fileName="counter"
    # Write value
    fos = open(fileName, 'w')
    fos.write(initialValue)
    fos.close()
    print "Initial counter value is " + initialValue
    # Execute increment
    increment(fileName)
    # Write new value
    fis = compss_open(fileName, 'r+')
    finalValue = fis.read()
    fis.close()
    print "Final counter value is " + finalValue

if __name__=='__main__':
    main_program()
