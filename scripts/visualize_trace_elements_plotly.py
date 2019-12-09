import requests
import plotly.graph_objects as go


def run_query(query):
    request = requests.post('http://localhost:8000/api/graphql', json={'query': query})
    if request.status_code == 200:
       return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

query = """
{  
  allMetal(country: "Cyprus", description: "Ore") {
    edges {
      node {
        id
        description
        source
        site
        country
        elementTraceAssayId {
          id
        }
      }
    }
  }

  allElements {
    edges {
      node {
        id
        copperPercent
        copperPpm
        arsenicPercent
        arsenicPpm
        silverPercent
        silverPpm
        nickelPpm
        nickelPercent
        cobaltPercent
        cobaltPpm
        goldPercent
        goldPpm
        zincPercent
        zincPpm
        sulfurPercent
        sulfurPpm
        antimonyPercent
        antimonyPpm
        tinPercent
        tinPpm
        leadPercent
        leadPpm
        seleniumPercent
        seleniumPpm
        telluriumPercent
        telluriumPpm
        bismuthPercent
        bismuthPpm
        ironPercent
        ironPpm
      }
    }
  }

}
"""

result = run_query(query)

data = {
    'Copper_wt_percent': [],
    'Silver_wt_percent': [],
    'color': [],
    'size': []
}

all_metal = result['data']['allMetal']['edges']
all_elements = result['data']['allElements']['edges']
trace_elements = { }

for node in all_elements:
    trace_elements[node['node']['id']] = node['node']

for node in all_metal:
    if node['node']['elementTraceAssayId']:
        elements = trace_elements[node['node']['elementTraceAssayId']['id']]
        
        if elements['copperPercent'].find('<') > -1:
            elements['copperPercent'].replace('<', '')
            metal1 = elements['copperPercent'].replace('<', '')
        else:
            metal1 = elements['copperPercent']
        
        # if elements['silverPercent'].find('<') > -1:
        #     elements['silverPercent'].replace('<', '')
        #     metal2 = elements['silverPercent'].replace('<', '')
        # else:
        #     metal2 = elements['silverPercent']
        
        # print(metal1, metal2)
        # if elements['copperPpm'].find('<') > -1:
        #     elements['copperPpm'].replace('<', '')
        #     metal1 = elements['copperPpm'].replace('<', '')
        # else:
        #     metal1 = elements['copperPpm']
        
        if elements['silverPpm'].find('<') > -1:
            elements['silverPpm'].replace('<', '')
            metal2 = elements['silverPpm'].replace('<', '')
        else:
            metal2 = elements['silverPpm']

        # Divide by 10000 to convert to ppm and then 100 for % plot
        # if float(metal1) > 0 and float(metal2) > 0:
        # data['Copper_wt_percent'].append(float(metal1)/1000000)
        data['Silver_wt_percent'].append(float(metal2)/1000000)       
        data['Copper_wt_percent'].append(float(metal1)/100)
        # data['Silver_wt_percent'].append(float(metal2)/100)
        data['color'].append('Black')
        data['size'].append(15)

fig = go.Figure(data=go.Scatter(
  x=data['Copper_wt_percent'], 
  y=data['Silver_wt_percent'], 
  mode='markers',
  marker=dict(size=data['size'], color=data['color'])
))

fig.update_layout(
    title="Copper vs. Silver Weight % in Cyprus Ore",
    xaxis=dict(tickformat=".2%"),
    yaxis=dict(tickformat=".3%"),
    xaxis_title="Cu wt(%)",
    yaxis_title="Ag wt(%)",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="black"
    )
)

fig.show()
