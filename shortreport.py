import json

with open("/tmp/tsunami-output.json", 'r', encoding='utf-8') as data_file:
    data = json.load(data_file)


    status = data['scanStatus']
    ip = data['scanFindings'][0]['networkService']['networkEndpoint']['ipAddress']['address']
    port = data['scanFindings'][0]['networkService']['networkEndpoint']['port']['portNumber']
    software = data['scanFindings'][0]['networkService']['serviceContext']['webServiceContext']['software']['name']
    issue = data['scanFindings'][0]['vulnerability']['title']
    severity = data['scanFindings'][0]['vulnerability']['severity']
    info = data['scanFindings'][0]['vulnerability']['description']
    recom = data['scanFindings'][0]['vulnerability']['recommendation']
    dtime = data['scanStartTimestamp']
    if issue :
        print('Scan Status {}, \nIp Address : {} \nPort Number : {}\n'
              'Software : {}\nVulnerability : {} \nSeverity : {}\n'
              'Description : {}\nRecommendation : {} \nScan run time : {}'
              '  '.format(status, ip, port, software, issue, severity, info, recom, dtime))
    else:
        print('There are no vulnerability')
