from sheetgo.api.app import initialize
from sheetgo.main_module import MODULES

application = initialize(modules=MODULES)

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
