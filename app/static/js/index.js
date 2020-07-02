//拓扑图
(function () {
    var dom = document.getElementById("showresult");
    var myChart = echarts.init(dom);
    option = null;
    myChart.hideLoading();
    $.get('static/data/data.xml', function (xml) {
        myChart.hideLoading();
        var graph = echarts.dataTool.gexf.parse(xml);
        var categories = [];
        categories[0] = '未传播点'
        graph.nodes.forEach(function (node) {
            node.itemStyle = null;
            node.symbolSize = 10;
            node.value = node.symbolSize;
            node.category = node.attributes.modularity_class;
            node.x = node.y = null;
            node.draggable = true;
           });
        option = {
            color:['#44f82c','#ff0404','#c23531','#2f4554', '#61a0a8', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3'],
            title: {
                text: 'IPV6网络拓扑图',
                subtext: '',
                top: 'bottom',
                left: 'right',
                textStyle:{color: "#fff"}
            },
            tooltip: {},
            animation: true,
            series : [
                {
                    name: 'IPV6',
                    type: 'graph',
                    layout: 'force',
                    data: graph.nodes,
                    links: graph.links,
                    categories: categories,
                    //focusNodeAdjacency : true,
                    roam: 'scale',
                    label: {
                        position: 'right'
                    },
                    force: {
                        repulsion: 50
                    }
                }
            ]
        };
        myChart.setOption(option);
        window.addEventListener('resize',function(){
            myChart.resize();
        })
    }, 'xml');
    if (option && typeof option === "object") {
        myChart.setOption(option,true);
    }
})();

//图表1
(function(){
    var dom = document.getElementById("first");
    var myChart = echarts.init(dom);
    //配置图表
    option = {
        color: ['#2f89cf'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        grid: {
            left: '0%',
            right: '0%',
            top: '10px',
            bottom: '4%',
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
                axisTick: {
                    alignWithLabel: true,
                },
                //x轴文字样式
                axisLabel: {
                    color: "rgba(255,255,255,0.6)",
                    fontSize: "12"
                },
                axisLine: {
                    show: false
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                axisLabel: {
                    color: "rgba(255,255,255,0.6)",
                    fontSize: "12"
                },
                axisLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,0.1)",
                        width: "2"
                    }
                },
                //y分割线
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,0.1)",
                        width: "1"
                    }
                }
            }
        ],
        series: [
            {
                name: '直接访问量',
                type: 'bar',
                barWidth: '35%',
                data: [400, 560, 373, 401, 560, 450, 470],
                itemStyle: {
                    barBorderRadius: 5
                }
            }
        ]
    };
    myChart.setOption(option);
    window.addEventListener('resize',function(){
        myChart.resize();
    })
})();

//图表3
(function(){
    var dom = document.getElementById("third");
    var myChart = echarts.init(dom);
    var mycolor = ["green","#1089E7","#F57474","#56D0E3","#F88448","#8878F6"]
    option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        grid: {
            top: '5%',
            left: '10%',
            bottom: '5%',
            //containLabel: true
        },
        xAxis: {
            show: false
        },
        yAxis: [
            {
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                axisLabel: {
                    color: "rgba(255,255,255,0.6)"
                },
                type: 'category',
                data: ['其他', '河南', '山东', '江苏', '河北', '甘肃']
            },
            {
                show: true,
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                axisLabel: {
                    color: "rgba(255,255,255,0.6)"
                },
                type: 'category',
                data: ['2654', '964', '876', '836', '940', '1023']
            }
        ],
        series: [
            {//条形
                name: '2018年',
                type: 'bar',
                data: [2555, 952, 799, 821, 920, 1024],
                itemStyle: {
                    barBorderRadius: 20,
                    color: function(params){
                        return mycolor[params.dataIndex]
                    }
                },
                yAxisIndex: 0,
                //柱子间距
                barCategoryGap: 50,
                //宽度
                barWidth:12,
                label: {
                    show: true,
                    position: 'inside',
                    formatter: "{c}"
                }
            },
            {
                name: '2019年',
                type: 'bar',
                yAxisIndex: 1,
                //柱子间距
                barCategoryGap: 50,
                //宽度
                barWidth:15,
                data: [2555, 952, 799, 821, 920, 1024],
                itemStyle: {
                    barBorderRadius: 15,
                    borderColor: "rgba(255,255,255,0.7)",//"#00c1de",
                    borderWidth: 3,
                    color: 'none',
                },
            }
        ]
    };
    myChart.setOption(option);
    window.addEventListener('resize',function(){
        myChart.resize();
    })
})();

//图2




(function(){
    var dom = document.getElementById("second");
    var myChart = echarts.init(dom);

    option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross',
                label: {
                    backgroundColor: '#6a7985'
                }
            }
        },
        grid: {
            left: '10',
            right: '15',
            bottom: '10',
            top: '30',
            containLabel: true
        },
        color: ['#00d887','#0184d5'],
        legend: {
            data: ['校内流量','校外流量'],
            textStyle: {
                color: "rgba(255,255,255,0.7)"
            }
        },
        xAxis: [
            {
                type: 'category',
                boundaryGap: false,
                data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
                axisLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,0.1)"
                    }
                },
                axisLabel: {
                    textStyle: {
                        color: "rgba(255,255,255,0.7)"
                    }
                },
            }
        ],
        yAxis: [
            {
                type: 'value',
                axisLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255,0.1)'
                    }
                },
                axisLabel: {
                    textStyle: {
                        color: "rgba(255,255,255,0.7)"
                    }
                },
                splitLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255,0.1)'
                    }
                }
            }
        ],
        series: [
            {
                name: '校内流量',
                type: 'line',
                smooth: 'true',
                data: [250, 380, 220, 234, 350, 220, 290],
                // lineStyle: {
                //     color: "#00d887",
                //     width: '2'
                // },
                symbol: "circle",
                symbolSize: '5',
                showSymbol: false,
                areaStyle: {
                    //设置渐变
                    color: new echarts.graphic.LinearGradient(
                        0,0,0,1,
                        [
                            {
                                offset: 0,
                                color: "rgba(0,216,135,0.4)"
                            },
                            {
                                offset: 0.8,
                                color: "rgba(0,216,135,0.1)"
                            }
                        ],
                        false
                    ),
                    shadowColor: "rgba(0,0,0,0,0.1)"
                }
            },
            {
                name: '校外流量',
                type: 'line',
                smooth: 'true',
                itemStyle: {
                    color: "#0184d5",
                    borderColor: "rgba(221,220,107,0.1)",
                    borderWidth: "8"
                },
                data: [150, 180, 153, 167, 210, 230, 180],
                areaStyle: {
                    //设置渐变
                    color: new echarts.graphic.LinearGradient(
                        0,0,0,1,
                        [
                            {
                                offset: 0,
                                color: "rgba(1,132,213,0.4)"
                            },
                            {
                                offset: 0.8,
                                color: "rgba(1,132,213,0.1)"
                            }
                        ],
                        false
                    ),
                    shadowColor: "rgba(0,0,0,0,0.1)"
                },
                symbol: "circle",
                symbolSize: '5',
                showSymbol: false,
            }
        ]
    };
    myChart.setOption(option);
    window.addEventListener('resize',function(){
        myChart.resize();
    })
})();

//图4
(function(){
    var dom = document.getElementById("fourth");
    var myChart = echarts.init(dom);
    option = {
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        // legend: {
        //     right: '0',
        //     top: '0',
        //     orient: 'vertical',
        //     data: ['教学科研人员', '在站博士后', '教授等正高职', '研究生导师'],
        //     textStyle :{
        //         color: 'rgba(255,255,255,0.7)'
        //     }
        // },
        series: [
            {
                name: '职业分布',
                type: 'pie',
                radius: [40, 60],
                center: ['50%', '50%'],
                roseType: 'area',
                emphasis: {
                    label: {
                        show: true
                    }
                },
                data: [
                    {value: 2303, name: '教学科研人员'},
                    {value: 169, name: '在站博士后'},
                    {value: 696, name: '教授等正高职'},
                    {value: 1845, name: '研究生导师'}
                ]
            }
        ]
    };
    myChart.setOption(option);
    window.addEventListener('resize',function(){
        myChart.resize();
    })
})();


