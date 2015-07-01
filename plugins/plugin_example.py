# This is a sample plugin used for flexible reporting of metrics
#
# Graphios makes the call `get_metrics(perfdata, nag)` where
#
#    nag: contains all the fields defined in the nagios log
#    perfdata: is just nag.PERFDATA
# 
# It expects the output to be a list of metric paths and values and 
# Graphios will use the nag.TIMET timestamp to form the correct metric
#
# For example: 
#
#   get_metrics() -> [ ( "stats.server1.cpu", .10 ) ]
# 
# Would result in the following metric:
#
#   stats.server1.cpu .10 <nag.TIMET>
#
# Graphios will append the timestamp, only the path, and value pair must be
# returned
#
    
def get_metrics(perfdata, nag):
    """ 
        returns a [(<path>, <value>)] where each is the metric to send to carbon
    """

    results = []
    for metric in perfdata.split():
        label = perfdata.split('=')[0]
        path = "%s.%s.%s" % (nag.GRAPHITEPREFIX, nag.HOSTNAME, label)
        value = nag.VALUE
        results.append((path, value))

    return results
