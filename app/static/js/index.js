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
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
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
                data: [10, 52, 200, 334, 390, 330, 220],
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
                data: ['巴西', '印尼', '美国', '印度', '中国', '日本']
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
                data: ['127', '758', '644', '423', '843', '123']
            }
        ],
        series: [
            {//条形
                name: '2011年',
                type: 'bar',
                data: [50, 75, 80, 63, 45, 78],
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
                    formatter: "{c}%"
                }
            },
            {
                name: '2012年',
                type: 'bar',
                yAxisIndex: 1,
                //柱子间距
                barCategoryGap: 50,
                //宽度
                barWidth:15,
                data: [100, 100, 100, 100, 100, 100],
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
            data: ['邮件营销','视频广告'],
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
                name: '邮件营销',
                type: 'line',
                smooth: 'true',
                data: [120, 380, 101, 134, 90, 230, 210],
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
                name: '视频广告',
                type: 'line',
                smooth: 'true',
                itemStyle: {
                    color: "#0184d5",
                    borderColor: "rgba(221,220,107,0.1)",
                    borderWidth: "8"
                },
                data: [150, 180, 201, 154, 190, 330, 410],
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
        legend: {
            right: '0',
            top: '0',
            orient: 'vertical',
            data: ['学生', '老师', '记者', '医生', '其他'],
            textStyle :{
                color: 'rgba(255,255,255,0.7)'
            }
        },
        series: [
            {
                name: '职业分布',
                type: 'pie',
                radius: [20, 100],
                center: ['50%', '50%'],
                roseType: 'area',
                emphasis: {
                    label: {
                        show: true
                    }
                },
                data: [
                    {value: 10, name: '学生'},
                    {value: 16, name: '老师'},
                    {value: 15, name: '记者'},
                    {value: 25, name: '医生'},
                    {value: 40, name: '其他'},
                ]
            }
        ]
    };
    myChart.setOption(option);
    window.addEventListener('resize',function(){
        myChart.resize();
    })
})();


