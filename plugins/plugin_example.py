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
    
def get_metrics(perfdata, nag):
    """ 
        returns a [(<path>, <value>)] where each is the metric to send to carbon
    """

    path = "%s.%s.%s.%s" % (nag.GRAPHITEPREFIX, nag.HOSTNAME, nag.GRAPHITEPOSTFIX, nag.LABEL)
    value = nag.VALUE

    return [ (path, value) ]
