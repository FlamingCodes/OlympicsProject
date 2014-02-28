    <table id="datatable1" class="datatable">
                    <thead>
                    %for head in datatable[0]:
                        <th>{{head}}</th>
                    %end
                    </thead>
                    %x = 0
                    %for col in datatable[1]:
                        %x+=1
                        %y= x % 2
                        %if y > 0:
                            <tr>
                                %for i in col:
                                    <td class="colored">{{i}}</td>
                                %end
                            </tr>
                        %else:
                             <tr>
                                %for i in col:
                                    <td>{{i}}</td>
                                %end
                            </tr> 
                        %end
                    %end
                </table>