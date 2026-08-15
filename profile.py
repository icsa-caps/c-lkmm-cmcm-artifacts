import geni.portal as portal
import geni.rspec.pg as pg

# Create a Request object to start building the RSpec
request = portal.context.makeRequestRSpec()

# Request a single bare-metal node
node = request.RawPC("node")

# Force the node to be a d710 hardware type
node.hardware_type = "d710"

# Assign the standard Debian 13 image
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD"

# Print the RSpec to the portal
portal.context.printRequestRSpec()
