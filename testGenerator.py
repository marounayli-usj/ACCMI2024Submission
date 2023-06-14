from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
template = env.get_template('testTemplate.j2')


# filename,base_url,testcases
def generateScript(payload):
    print("The size of sentences is ", len(payload["sentences"]) )
    print(payload["sentences"])
    output = template.render(baseurl= payload["base_url"], sequence = payload["sentences"])
    with open('generatedTests/'+payload["test_name"]+'.py', 'w') as f:
        f.write(output)