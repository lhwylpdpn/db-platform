/**
 * Silence
 */
;
$(function() {
    var Filter = function() {
        this.init();

    };

    //已选数据
    // var $selectedArr = [];
    // $('#FilterTagSelected').find('a').each(function(){
    //     if ($(this).data('channel') || $(this).data('agent') || $(this).data('staff')){
    //         $selectedArr.push($(this).data('channel') || $(this).data('agent') || $(this).data('staff'));
    //     }
    // });

    Filter.prototype = {
        //初始化
        init: function() {
            this.initLoad();
            this.clearData();
            this.filterTag();
            this.moreDate();
            this.wordFilter();
        },
        initLoad:function(){
            this.loadData('platform','staff=','channel_name=','agent=');
            this.loadData('channel_name','platform=','staff=','agent=');
            this.loadData('agent','platform=','channel_name=','staff=');
            this.loadData('staff','platform=','channel_name=','agent=');
        },
        //载入数据
        loadData: function(a,b,c,d) {
            var url,
                dataBox,
                self = this;
            if (a=='platform'){dataBox='List01';}
            if (a=='channel_name'){dataBox='List02';}
            if (a=='agent'){dataBox='List03';}
            if (a=='staff'){dataBox='List04';}
            url = 'analyzeTJ?'+b+'&'+c+'&'+d+'&tjtype='+a;
                        console.log(url);

            $.getJSON(url, function(data){
                self.renderData(dataBox,data)
            });
        },
        //数据写入
        renderData:function(container,data){
            var initialList=[];
            $('#'+container).find('.list').empty();
            //写入数据
            $(data).each(function(i){
                var dataName='',dataVaule='';
                if (container=='List01'){
                    dataName= "data-platform="+data[i].platform;
                    dataVaule= data[i].platform;
                }
                if (container=='List02'){
                    dataName= "data-channel="+data[i].channel_name;
                    dataVaule= data[i].channel_name;
                }
                if (container=='List03'){
                    dataName= "data-agent="+data[i].agent;
                    dataVaule= data[i].agent;
                }
                if (container=='List04'){
                    dataName= "data-staff="+data[i].staff;
                    dataVaule= data[i].staff;
                }
                $('#'+container).find('.list').append('<li><a class="filter-tag" href="javascript:;" data-initial="'+data[i].initial+'" '+dataName+'>'+dataVaule+'<i></i></a></li>');
                if(initialList.indexOf(data[i].initial) == -1){
                    initialList.push(data[i].initial);
                }
            });
            //写入首字母
            initialList.sort();
            $('#'+container).find('.initial').empty().append('<li data-value="all" onclick="selectAll(this);">All</li>');
            $(initialList).each(function(i){
                $('#'+container).find('.initial').append('<li data-value="'+initialList[i]+'">'+initialList[i]+'</li>');

            });
            //反写已选状态
            $('#FilterTagSelected').find('a').each(function(){
                var aText = $(this).text(),
                    aData = '';
                if($(this).data('platform')){aData='platform'}
                if($(this).data('channel_name')){aData='channel_'}
                if($(this).data('agent')){aData='agent'}
                if($(this).data('staff')){aData='staff'}
                $('#FilterQueryList').find('a').each(function(){
                    if($(this).text()==aText && $(this).data(aData)){$(this).addClass('selected');}
                });
            });
            //0 click 清除 data-open
        },
        //清除数据
        clearData:function(){
            var self = this;
            //全部清除
            $('#FilterQueryClear').on('click',function(){
                $("#FilterTagSelected li").slice(1).remove();
                $('.any a').trigger('click');
                $('.filterlist').removeAttr('data-open');
                $('.filterlist').removeData('open');
                self.initLoad();
            });
            //单条清除
            $('#FilterTagSelected').on('click','i',function(){
                var closeText = $(this).parent().text(),
                    closeData = '';
                if($(this).parent().data('platform')){closeData='platform'}
                if($(this).parent().data('channel_name')){closeData='channel_name'}
                if($(this).parent().data('agent')){closeData='agent'}
                if($(this).parent().data('staff')){closeData='staff'}
                $('#FilterQueryList').find('a').each(function(){
                    if($(this).text()==closeText && $(this).data(closeData)){
                        $(this).trigger('click');
                    }
                });
            });
        },
        //选中数据
        filterTag: function() {
            var self = this;
            $('#FilterQueryList .list').on('click','a',function(){
                //tag状态&click
                if($(this).hasClass('selected')){
                    $(this).removeClass('selected');
                    var tagText = $(this).text(),
                        tagData = $(this).parents('.filterlist').data('value');
                    $('#FilterTagSelected').find('a').each(function(){
                        if($(this).text()==tagText && $(this).data(tagData)){
                            $(this).parent().remove();
                        }
                    })
                }else{
                    $(this).addClass('selected');
                    $(this).parents('li').clone().appendTo('#FilterTagSelected');
                };
                //联动标识
                var openNum=0;
                $('#FilterQueryList').find('.filterlist').each(function(){
                    if ($(this).data('open')){
                        openNum++
                    }
                });
                if(openNum==0){
                    $(this).parents('.filterlist').attr('data-open','1');
                }
                if(openNum==1 && !$(this).parents('.filterlist').data('open')){
                    $(this).parents('.filterlist').attr('data-open','2');
                }
                //联动load
                var idValue = $(this).parents('.filterlist').data('value'),
                    idOpen = $(this).parents('.filterlist').data('open'),
                    valueList = '',
                    platformList = '',
                    channelList = '',
                    agentList = '',
                    staffList = '';
                $(this).parents('#FilterQueryList').find('.filterlist').each(function(){
                    var key = $(this).data('value'),
                        valueList='';
                    $(this).find('.list a').each(function(){
                        if($(this).hasClass('selected')){
                            valueList=valueList+$(this).text()+',';
                        }
                    });
                    valueList = valueList.substr(0, valueList.length - 1);
                    if (key=='platform'){
                        platformList='platform='+valueList;
                    };
                    if (key=='channel_name'){
                        channelList='channel_name='+valueList;
                    };
                    if (key=='agent'){
                        agentList='agent='+valueList;
                    };
                    if (key=='staff') {
                        staffList='staff='+valueList;
                    };
                });
                //platform
                if (idValue=='platform'){
                    if (idOpen==1) {
                        self.loadData('channel_name',platformList,staffList,agentList);
                        self.loadData('agent',platformList,staffList,channelList);
                        self.loadData('staff',platformList,agentList,channelList);
                    };
                    if (idOpen==2) {
                        var id='';
                        $('#FilterQueryList').find('.filterlist').each(function(){
                            if (!$(this).data('open')){
                                id= $(this).data('value');
                            }
                        });
                        if (id=='channel_name'){
                            self.loadData('channel_name',platformList,staffList,agentList);
                        };
                        if (id=='agent'){
                            self.loadData('agent',platformList,staffList,channelList);
                        };
                        if (id=='staff') {
                            self.loadData('staff',platformList,agentList,channelList);
                        };
                    };
                };
                //channel
                if (idValue=='channel_name'){
                    if (idOpen==1) {
                        self.loadData('platform',channelList,staffList,agentList);
                        self.loadData('agent',platformList,staffList,channelList);
                        self.loadData('staff',platformList,agentList,channelList);
                    };
                    if (idOpen==2) {
                        var id='';
                        $('#FilterQueryList').find('.filterlist').each(function(){
                            if (!$(this).data('open')){
                                id= $(this).data('value');
                            }
                        });
                        if (id=='platform'){
                            self.loadData('platform',channelList,staffList,agentList);
                        };
                        if (id=='agent'){
                            self.loadData('agent',platformList,staffList,channelList);
                        };
                        if (id=='staff') {
                            self.loadData('staff',platformList,agentList,channelList);
                        };
                    };
                };
                //agent
                if (idValue=='agent'){
                    if (idOpen==1) {
                        self.loadData('platform',channelList,staffList,agentList);
                        self.loadData('channel_name',platformList,staffList,agentList);
                        self.loadData('staff',platformList,agentList,channelList);
                    };
                    if (idOpen==2) {
                        var id='';
                        $('#FilterQueryList').find('.filterlist').each(function(){
                            if (!$(this).data('open')){
                                id= $(this).data('value');
                            }
                        });
                        if (id=='platform'){
                            self.loadData('platform',channelList,staffList,agentList);
                        };
                        if (id=='agent'){
                            self.loadData('channel_name',platformList,staffList,agentList);
                        };
                        if (id=='staff') {
                            self.loadData('staff',platformList,agentList,channelList);
                        };
                    };
                };
                //staff
                if (idValue=='staff'){
                    if (idOpen==1) {
                        self.loadData('platform',channelList,staffList,agentList);
                        self.loadData('channel_name',platformList,staffList,agentList);
                        self.loadData('agent',platformList,staffList,channelList);
                    };
                    if (idOpen==2) {
                        var id='';
                        $('#FilterQueryList').find('.filterlist').each(function(){
                            if (!$(this).data('open')){
                                id= $(this).data('value');
                            }
                        });
                        if (id=='platform'){
                            self.loadData('platform',channelList,staffList,agentList);
                        };
                        if (id=='agent'){
                            self.loadData('agent',platformList,staffList,channelList);
                        };
                        if (id=='channel_name') {
                            self.loadData('channel_name',platformList,staffList,agentList);
                        };
                    };
                };


                //不限状态
                var selectedNum = 0;
                $(this).parents('.list').find('a').each(function(){
                    if($(this).hasClass('selected')){
                        $(this).parents('.checkboxF').find('.any a').removeClass('selected');
                        selectedNum ++
                    }
                    if (selectedNum==0){
                        $(this).parents('.checkboxF').find('.any a').addClass('selected');
                    }
                });
                //不限click
                $('.filter-unlimit').on('click',function(){
                    if(!$(this).hasClass('selected')){
                        $(this).parents('.checkboxF').find('.list a').removeClass('selected');
                        $(this).addClass('selected');
                        var value = $(this).parents('.filterlist').data('value');
                        $('#FilterTagSelected').find('a').each(function(){
                            if($(this).data(value)){
                                $(this).parent().remove();
                            }
                        });

                    }
                });
                //清除已选tag的class
                $('#FilterTagSelected li a').removeClass('filter-tag selected');
            });
        },
        //展开更多
        moreDate: function() {
            $('.filter-more').on('click',function(){
                var list = $(this).parents('.hotel-filter-list');
                if(list.hasClass('hotel-filter-list-min')){
                    list.removeClass('hotel-filter-list-min');
                }else{
                    list.addClass('hotel-filter-list-min');
                    list.find('.list li').show();
                }
            });
        },
        //字母筛选
        wordFilter: function() {
            $('.initial').on('mouseover','li',function(){
                var tagInitial = $(this).data('value');
                if(tagInitial=='all'){
                    $(this).parents('.checkboxF').find('.list li').show();
                }else{
                    $(this).parents('.checkboxF').find('.list li').each(function(){
                        $(this).hide();
                        if($(this).find('a').data('initial')==tagInitial){
                             $(this).show();
                        }
                    });
                }
            });
        }
    };
    new Filter();
});
function selectAll( obj ){
    $(obj).parents("ul").next("ul").find("a").click();
}
