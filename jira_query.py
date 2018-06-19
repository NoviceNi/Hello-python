# coding=utf8
import optparse
import json
import urllib
import sys
import csv
import time
import datetime


from restkit import Resource, BasicAuth, request

rd_finish = 'customfield_15300'
qa_kickoff = 'customfield_15001'
qa_finish = 'customfield_10032'
stroy_point = 'customfield_10408'
sprint='customfield_10300'
epicnum='customfield_10301'
noplan="自测"
develop="开发中"
delay="延期："
def fetcher_factory(url, auth):
    resource = Resource(url, pool_instance=None, filters=[auth])
    response = resource.get(headers={'Content-Type': 'application/json',"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36"})
    if response.status_int == 200:
        # Not all resources will return 200 on success. There are other success status codes. Like 204. We've read
        # the documentation for though and know what to expect here.
        issue = json.loads(response.body_string())
        return issue
    else:
        return None

def time_differ(date1,date2):
     if date1 =="None":
         return noplan.decode("utf8")
     if date1 is None:
         return noplan.decode("utf8")
     if not (date2 and date1) is None :
        if  not date1 is None:
            date1f = datetime.datetime.strptime(date1, "%Y-%m-%d")
            date2f = datetime.datetime.strptime(date2, "%Y-%m-%d")
            if date1f < date2f:
                return  u'延期："%s"'%(date2f - date1f).days
            else:
              return u"正常提测"
        else:
            return noplan.decode("utf8")
     #if date1 is None and date2 is not None:
       #  return"No plan time"
     else:
         return develop.decode("utf8")

def get_epic(id):
    parser = optparse.OptionParser()
    auth = BasicAuth(options.user, options.password)
    jira_url = u'http://jira.tuniu.org/rest/api/2/issue/' + id
    issue_fetcher = fetcher_factory(jira_url, auth)
    response =issue_fetcher;
    j1=json.dumps(response)
    j2 = json.loads(j1)
    field=j2['fields']
    result =field['summary']
    print result
    return result


def parse_result(data):
    total = data['total']
    # print 'total is %s' % total
    output = dict()
    issues = data['issues']
    for issue in issues:
        output[issue['key']] = {'rd_finish':None,'qa_kickoff':None,'qa_finish':None,u'开始开发时间':None,u'实际提测时间':None,u'测试完成时间':None,u'主题':None,'stroy_point':None,'迭代名称':None,u'提测状态':None,'EpicLink':None,u'JiraLink':None,u'EpicName':None}
        print issue['key']
        #sprint名称获取
        name1=issue['fields'][sprint]
        namestart=name1[0].find("name=")+5
        nameend=name1[0].find(",startDate")
        sprintname=name1[0][namestart:nameend]
        #计划提测时间
        starttest=issue['fields'][qa_kickoff]
        if starttest is None:
            output[issue['key']][u'提测状态'] = noplan.decode("utf8")
        if starttest is not None:
            if starttest<time.strftime('%Y-%m-%d',time.localtime(time.time())):
               output[issue['key']][u'提测状态'] = u"延期"
            else:
                output[issue['key']][u'提测状态'] = develop.decode("utf8")
        output[issue['key']]['rd_finish'] = issue['fields'][rd_finish]
        output[issue['key']]['qa_kickoff'] = issue['fields'][qa_kickoff]
        output[issue['key']]['qa_finish'] = issue['fields'][qa_finish]
        output[issue['key']][u'主题'] = issue['fields']['summary']
        output[issue['key']]['stroy_point'] = issue['fields'][stroy_point]
        output[issue['key']][u'迭代名称'] = sprintname
        output[issue['key']]['EpicLink']=issue['fields'][epicnum]
        epicno=issue['fields'][epicnum]
        if epicno is None:
            output[issue['key']]['EpicName'] = "Others"
        else:
            en=get_epic(epicno)
            output [issue['key']]['EpicName']=en

        output[issue['key']]['JiraLink']=u'http://jira.tuniu.org/browse/' + issue['key']
        print output[issue['key']]['JiraLink']
        for history in issue['changelog']['histories']:
            if history['items'][0]['field'] == 'status':
                if (history['items'][0]['fromString'] == u'待开发' and history['items'][0]['toString'] == u'开发中'):
                    output[issue['key']][u'开始开发时间'] = history['created']
                    if output[issue['key']][u'开始开发时间']:
                        output[issue['key']][u'开始开发时间'] = output[issue['key']][u'开始开发时间'].split(':')[0]

                if (history['items'][0]['fromString'] == u'开发中'and history['items'][0]['toString'] == u'待验收'):
                    output[issue['key']][u'实际提测时间'] = history['created']
                    if output[issue['key']][u'实际提测时间']:
                        output[issue['key']][u'实际提测时间'] = output[issue['key']][u'实际提测时间'].split(':')[0]
                        actuallytest = history['created']
                        a1=actuallytest.find("T")
                        a2=actuallytest[0:a1]
                        delaytime=time_differ(starttest,a2)
                        output [issue['key']][u'提测状态']=delaytime
                        print delaytime
                if (history['items'][0]['fromString'] == u'验收中'and history['items'][0]['toString'] == u'待上线'):
                    output[issue['key']][u'测试完成时间'] = history['created']
                    if output[issue['key']][u'测试完成时间']:
                        output[issue['key']][u'测试完成时间'] = output[issue['key']][u'测试完成时间'].split(':')[0]
 
    return output


def parse_args():
    parser = optparse.OptionParser()
    parser.add_option('-u', '--user', dest='user', default='your name ', help='Username to access JIRA')
    parser.add_option('-p', '--password', dest='password', default='your password', help='Password to access JIRA')
    parser.add_option('-c', '--project', dest='project', default=u'S_内容', help='project name')
    parser.add_option('-i', '--issuetype', dest='issuetype', default=u'业务需求,技术需求', help='issuetype name')
    parser.add_option('-s', '--sprint', dest='sprint', default=u'9.35.0', help='9.35.0_象岛')

    return parser.parse_args()


if __name__ == '__main__':
    (options, args) = parse_args()

    # Basic Auth is usually easier for scripts like this to deal with than Cookies.
    auth = BasicAuth(options.user, options.password)
    a=options.project.decode("GBK")
    b=options.issuetype.decode("GBK")
    c= options.sprint.decode("GBK")
    jira_url = u'http://jira.tuniu.org/rest/api/2/search?expand=changelog&maxResults=1000&jql=' + urllib.quote(( u'project = "%s" AND issuetype in (%s) AND sprint = "%s"' % (a, b, c)).encode("utf-8"))
    issue_fetcher = fetcher_factory(jira_url, auth)
    result = parse_result(issue_fetcher)
    filename = u'_'.join([a, b, c, u'.csv'])
    writer = csv.writer(file(filename, 'wb'))
    writer.writerow([u'需求编号'.encode('gbk'),u'JiraLink'.encode('gbk'),u'迭代名称'.encode('gbk'),u'EpicLink'.encode('gbk'),u'EpicName',u'主题'.encode('gbk'),u'功能点数'.encode('gbk'),u'计划开始开发时间'.encode('gbk'), u'计划提测时间'.encode('gbk'),u'预计完成测试时间'.encode('gbk'),u'开始开发时间'.encode('gbk'),u'实际提测时间'.encode('gbk'),u'测试完成时间'.encode('gbk'),u'提测状态'.encode('gbk')])
    for key , data in result.items():
         writer.writerow([key,data[u'JiraLink'], data[u'迭代名称'].encode('gbk'),data[u'EpicLink'],data[u'EpicName'].encode('gbk'),data[u'主题'].encode('gbk'),data['stroy_point'],data['rd_finish'],data['qa_kickoff'],data['qa_finish'],data[u'开始开发时间'],data[u'实际提测时间'],data[u'测试完成时间'],data[u'提测状态'].encode('gbk')])
    
    #print result



