import http.server
import socketserver
import termcolor
import http.client
import json
from P1.Seq1 import Seq

PORT = 8080


class TestHandler(http.server.BaseHTTPRequestHandler):
    # -- This function will extract the information we are looking for within our URL,
    # which in this case will be the function that the user asks for:
    def extract_parameters(self, path):
        imp_params = dict()
        if '?' in path:
            parameters = path.split('?')[1]
            parameters = parameters.split(' ')[0]
            parameters_list = parameters.split('&')
            for keyvalue in parameters_list:
                key = keyvalue.split('=')[0]
                try:
                    value = keyvalue.split('=')[1]
                    imp_params[key] = value
                except IndexError:
                    print("IndexError in parameter")
        return imp_params

    def do_GET(self):
        json_option = False
        response_status = 200

        termcolor.cprint(self.requestline, 'green')

        server = 'rest.ensembl.org'
        # -- If nothing is written after connecting the port, the page will display completely:
        if self.path == '/':
            filename = 'index.html'
            with open(filename, 'r') as f:
                contents = f.read()
        # -- If the user asks for any of the following functions ('elifs'), different information will be given:
        elif '/listSpecies' in self.path:
            # -- Make the request:
            parameters = self.extract_parameters(self.path)
            connection = http.client.HTTPConnection(server)
            endpoint = 'info/species/'
            params = '?content-type=application/json'
            connection.request('GET', endpoint + params)
            req = connection.getresponse()

            # -- Process data:
            req_data = req.read().decode("utf-8")
            answer = json.loads(req_data)
            data_species = answer['species']
            try:
                if 'limit' in parameters and parameters['limit'] != '':
                    limit = int(parameters['limit'])
                else:
                    limit = len(data_species)

                # -- Now if 'json' is in the request, the contents will be given in this format
                if 'json' in parameters:
                    json_option = True
                    list_species = data_species[1:limit + 1]
                    contents = json.dumps(list_species)

                # -- If 'json' is not in the request, the contents will be an html file
                else:
                    contents = """
                                <html>
                                <body style="background-color: powderblue;">
                                <font face="Trebuchet MS">LIST OF SPECIES:
                                <ol>
                                """
                    # -- Iterate for each value until it reaches the desired limit
                    counter = 0
                    for specie in data_species:
                        contents = contents + f"""<li> {specie['display_name']} </li>"""
                        counter = counter + 1
                        if counter == limit:
                            break
                    contents = contents + """
                                </ol>
                                </font>
                                <br>
                                <a href="/">[Main page]</a>
                                </body>
                                </html>
                                """
                    connection.close()
            # -- This error raises if the input is not a number
            except ValueError:
                response_status = 404
                filename = open('error.html', 'r')
                contents = filename.read()

        elif '/karyotype' in self.path:
            parameters = self.extract_parameters(self.path)
            if 'specie' in parameters and parameters['specie'] != '':
                specie = parameters['specie']
                try:
                    # -- Make the request:
                    endpoint = '/info/assembly/'
                    params = '?content-type=application/json'
                    conn = http.client.HTTPConnection(server)
                    conn.request('GET', endpoint + specie + params)
                    req = conn.getresponse()

                    # -- Process data:
                    text_json = req.read().decode("utf-8")
                    answer = json.loads(text_json)
                    chromosome_data = answer['karyotype']

                    # -- Now if 'json' is in the request, the contents will be given in this format:
                    if 'json' in parameters:
                        json_option = True
                        contents = json.dumps(chromosome_data)

                    # -- If 'json' is not in the request, the contents will be an html file:
                    else:
                        contents = f"""
                                   <html>
                                   <body style="background-color: powderblue;">
                                   <font face="Trebuchet MS">
                                   <This is the karyotype information of the {specie}:
                                    <ul>"""
                        # -- Iterate on the chromosome_data so that we get the karyotype of the desired:
                        for specie in chromosome_data:
                            contents = contents + f"""<li> {specie} </li>"""

                        contents = contents + """
                                               </ul>
                                               </font>
                                               <br>
                                               <a href="/">[Main page]</a>
                                               </body>
                                               </html>
                                               """
                # -- This exception raises when the specie doesn't belong in the chromosome_data, so it doesn't exist:
                except KeyError:
                    response_status = 404
                    filename = open('error.html', 'r')
                    contents = filename.read()
            # -- This error raises if the input is left in blank:
            else:
                response_status = 404
                filename = open('error.html', 'r')
                contents = filename.read()

        elif '/chromosomeLength' in self.path:
            parameters = self.extract_parameters(self.path)

            if 'specie' and 'chromo' in parameters and parameters['specie'] != '' and parameters['chromo'] != '':
                specie = parameters['specie']
                chromosome = parameters['chromo']
                try:
                    # -- Make the request:
                    conn = http.client.HTTPConnection(server)
                    endpoint = '/info/assembly/'
                    params = '?content-type=application/json'
                    conn.request('GET', endpoint + specie + params)
                    req1 = conn.getresponse()

                    # -- Process data:
                    text_json = req1.read().decode("utf-8")
                    answer = json.loads(text_json)

                    chromosome_specie = answer['top_level_region']

                    # -- Now if 'json' is in the request, the contents will be given in this format
                    if 'json' in parameters:
                        json_option = True
                        chromosome_length = 0
                        # -- Here we iterate in chromosome_specie so that we get the length of the desired specie
                        for i in chromosome_specie:
                            if i['name'] == chromosome:
                                chromosome_length = str(i['length'])
                        # -- Then we create a dictionary to place all the information that we got with the iteration:
                        length_dictionary = dict()
                        length_dictionary['length'] = chromosome_length
                        contents = json.dumps(length_dictionary)

                    # -- If 'json' is not in the request, the contents will be an html file
                    else:
                        contents = f"""
                                   <html>
                                   <body style="background-color: powderblue;">
                                    <font face="Trebuchet MS">
                                    <p>This is the length of the {chromosome} chromosome of the {specie}:</p>"""
                        # -- Here we iterate in chromosome_specie so that we get the desired chromosome
                        # -- And the we take the value in the key 'length':
                        chromosome_length = 0
                        for i in chromosome_specie:
                            if i['name'] == chromosome:
                                chromosome_length = str(i['length'])

                        contents = contents + f"""
                                                <ul><li>{str(chromosome_length)}</li></ul>
                                               <br>
                                               <a href="/">[Main page]</a>
                                               </body>
                                               </html>
                                               """
                # -- This error raises if the input is not a number:
                except ValueError:
                    response_status = 404
                    filename = open('error.html', 'r')
                    contents = filename.read()
                # -- This exception raises when the specie doesn't belong in the chromosome_specie, so it doesn't exist:
                except KeyError:
                    response_status = 404
                    filename = open('error.html', 'r')
                    contents = filename.read()
            # -- This error raises if the input is left in blank:
            else:
                response_status = 404
                filename = open('error.html', 'r')
                contents = filename.read()

        elif '/geneSeq' in self.path:
            parameters = self.extract_parameters(self.path)

            if 'gene' in parameters and parameters['gene'] != '':
                gene = parameters['gene']
                try:
                    # -- Make the request:
                    conn = http.client.HTTPConnection(server)
                    endpoint1 = '/homology/symbol/human/'
                    params = '?content-type=application/json'
                    conn.request('GET', endpoint1 + gene + params)
                    req1 = conn.getresponse()

                    # -- Process data:
                    text_json = req1.read().decode("utf-8")
                    answer = json.loads(text_json)
                    id = answer['data'][0]['id']

                    # -- Make the request with the new endpoint:
                    endpoint2 = '/sequence/id/'
                    conn.request('GET', endpoint2 + id + params)
                    req1 = conn.getresponse()

                    # -- Process data:
                    text_json = req1.read().decode("utf-8")
                    answer = json.loads(text_json)
                    sequence = answer['seq']

                    # -- Now if 'json' is in the request, the contents will be given in this format:
                    if 'json' in parameters:
                        json_option = True
                        # -- A dictionary with the sequence is created, so it can display the info in that format:
                        seq_dictionary = dict()
                        seq_dictionary['seq'] = sequence
                        contents = json.dumps(seq_dictionary)

                    # -- If 'json' is not in the request, the contents will be an html file
                    else:
                        contents = f"""
                                   <html>
                                   <body style="background-color: powderblue;">
                                   <font face="Trebuchet MS">The sequence corresponding to gene {gene} is:</font>
                                    <br><br>
                                    {sequence}
                                    <br><br>
                                    <a href="/">[Main page]</a>
                                   </body>
                                   </html>
                                   """
                # -- This exception raises when the specie doesn't belong in the chromosome_data, so it doesn't exist:
                except KeyError:
                    response_status = 404
                    filename = open('error.html', 'r')
                    contents = filename.read()
            # -- This error raises if the input is left in blank:
            else:
                response_status = 404
                filename = open('error.html', 'r')
                contents = filename.read()

        elif '/geneInfo' in self.path:
            parameters = self.extract_parameters(self.path)
            if 'gene' in parameters and parameters['gene'] != '':
                gene = parameters['gene']
                try:
                    # -- Make the request:
                    conn = http.client.HTTPConnection(server)
                    endpoint1 = '/homology/symbol/human/'
                    params1 = '?content-type=application/json'
                    conn.request('GET', endpoint1 + gene + params1)
                    req1 = conn.getresponse()

                    # -- Process data:
                    text_json = req1.read().decode("utf-8")
                    answer = json.loads(text_json)
                    id = answer['data'][0]['id']

                    # -- Make the second request:
                    endpoint2 = '/overlap/id/'
                    params2 = '?feature=gene;content-type=application/json'
                    conn.request('GET', endpoint2 + id + params2)
                    req1 = conn.getresponse()

                    # -- Process the received data:
                    text_json = req1.read().decode("utf-8")
                    answer = json.loads(text_json)
                    start = answer[0]['start']
                    end = answer[0]['end']
                    length = end - start
                    chromosome = answer[0]['assembly_name']
                    # -- If 'json' is in the request, the contents will be given in this format:
                    if 'json' in parameters:
                        json_option = True
                        # -- We create a dictionary to store all the values for each type of info:
                        info_dictionary = dict()
                        info_dictionary['start'] = start
                        info_dictionary['end'] = end
                        info_dictionary['length'] = length
                        info_dictionary['chromosome'] = chromosome
                        contents = json.dumps(info_dictionary)
                    # -- If 'json' is not in the request, the contents will be an html file:
                    else:
                        contents = f"""
                                   <html>
                                   <body style="background-color: powderblue;">
                                   <font face="Trebuchet MS">
                                    <p>The information corresponding to gene {gene}</p>
                                    <li>START: {str(start)}</li>
                                    <li>END: {str(end)}</li>
                                   <li>ID: {str(id)} </li>
                                   <li>LENGTH: {str(length)} 
                                   <li>CHROMOSOME: {chromosome}
                                   </font>
                                   <br>
                                   <a href="/">[Main page]</a>
                                   </body>
                                   </html>
                                   """
                except KeyError:
                    response_status = 404
                    filename = open('error.html', 'r')
                    contents = filename.read()
            # -- This error raises if the input is left in blank
            else:
                response_status = 404
                filename = open('error.html', 'r')
                contents = filename.read()

        elif '/geneCalc' in self.path:
            parameters = self.extract_parameters(self.path)

            if 'gene' in parameters and parameters['gene'] != '':
                gene = parameters['gene']
                try:
                    # -- Make the request:
                    connection = http.client.HTTPConnection(server)
                    endpoint1 = '/homology/symbol/human/'
                    params = '?content-type=application/json'
                    connection.request('GET', endpoint1 + gene + params)
                    req1 = connection.getresponse()

                    # -- Process data:
                    text_json = req1.read().decode("utf-8")
                    answer = json.loads(text_json)
                    id = answer['data'][0]['id']

                    endpoint2 = '/sequence/id/'
                    connection.request('GET', endpoint2 + id + params)
                    req1 = connection.getresponse()

                    text_json = req1.read().decode("utf-8")
                    answer = json.loads(text_json)
                    sequence = answer['seq']
                    seq = Seq(sequence)
                    length = len(sequence)
                    percentageA = seq.percent('A')
                    percentageC = seq.percent('C')
                    percentageT = seq.percent('T')
                    percentageG = seq.percent('G')
                    # -- If 'json' is in the request, the contents will be given in this format:
                    if 'json' in parameters:
                        json_option = True
                        calc_dictionary = dict()
                        calc_dictionary['sequence'] = sequence
                        calc_dictionary['percentage A'] = percentageA
                        calc_dictionary['percentage C'] = percentageC
                        calc_dictionary['percentage T'] = percentageT
                        calc_dictionary['percentage G'] = percentageG
                        calc_dictionary['length'] = length
                        contents = json.dumps(calc_dictionary)

                    else:
                        contents = f"""
                                   <html>
                                   <body style="background-color: powderblue;">
                                   <font face="Trebuchet MS">
                                   <p>The sequence corresponding to gene {gene} is: </p>
                                    {sequence} 
                                    <p> The calculations are: </p>
                                    <li>TOTAL LENGTH: {str(length)}
                                    <li>PERCENTAGE OF A BASES: {str(percentageA)} 
                                    <li>PERCENTAGE OF C BASES: {str(percentageC)}
                                    <li>PERCENTAGE OF T BASES: {str(percentageT)}
                                    <li>PERCENTAGE OF G BASES: {str(percentageG)}
                                   </font>
                                    <br>
                                    <br>
                                    <a href="/">[Main page]</a>
                                   </body>
                                   </html>
                                   """
                except KeyError:
                    response_status = 404
                    filename = open('error.html', 'r')
                    contents = filename.read()
            # -- This error raises if the input is left in blank
            else:
                response_status = 404
                filename = open('error.html', 'r')
                contents = filename.read()

        elif '/geneList' in self.path:
            parameters = self.extract_parameters(self.path)
            if 'start' in parameters and parameters['start'] != '' and 'chromo' in parameters and parameters['chromo'] != '' and 'end' in parameters and parameters['end'] != '':
                chromosome = parameters['chromo']
                start = parameters['start']
                end = parameters['end']
                try:
                    # -- Make the request:
                    conn = http.client.HTTPConnection(server)
                    endpoint = "/overlap/region/human/"
                    params = "?content-type=application/json;feature=gene;feature=transcript;feature=cds;feature=exon"
                    conn.request("GET", endpoint + str(chromosome) + ":" + str(start) + "-" + str(end) + params)
                    r1 = conn.getresponse()

                    # -- Process data:
                    text_json = r1.read().decode("utf-8")
                    answer = json.loads(text_json)
                    # -- If 'json' is in the request, the contents will be given in this format:
                    if 'json' in parameters:
                        json_option = True
                        json_list = []
                        # -- Here, it iterates through the info received from ensembl until it reaches the
                        # 'feature_type' key, the information there will be stored and given in a json format
                        for element in answer:
                            if element['feature_type'] == 'gene':
                                gene_dictionary = dict()
                                gene_dictionary['name'] = element['external_name']
                                gene_dictionary['start'] = element['start']
                                gene_dictionary['end'] = element['end']
                                json_list.append(gene_dictionary)
                        contents = json.dumps(json_list)

                    else:
                        contents = f"""
                                <html>
                                <body style= "background-color: powderblue;">
                                <font face="Trebuchet MS">
                                <p>The names of the genes located in chromosome {chromosome} from {start} to {end} are: </p>
                                """
                        for element in answer:
                            if 'feature_type' in element and (element['feature_type'] == 'gene'):
                                contents = contents + f"""<li> {element['external_name']} </li>"""

                        contents = contents + """
                                                </font>
                                                <br>
                                                <br>
                                                <a href="/">[Main page]</a>
                                                </body>
                                                </html>
                                                """
                # -- This error raises if the input is not a number
                except ValueError:
                    response_status = 404
                    filename = open('error.html', 'r')
                    contents = filename.read()
            # -- This error raises if the input is left in blank
            else:
                response_status = 404
                filename = open('error.html', 'r')
                contents = filename.read()
        # -- This error raises if the URL doesn't include an existent function:
        else:
            response_status = 404
            filename = 'error.html'
            with open(filename, 'r') as f:
                contents = f.read()

        self.send_response(response_status)  # -- Status line: OK!
        # Define the content-type header:
        if json_option is True:
            self.send_header('Content-Type', 'application/json')
        else:
            self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()
        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler
socketserver.TCPServer.allow_reuse_address = True
# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
