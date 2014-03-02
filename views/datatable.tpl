    <table id="datatable1" class="datatable">
                    <thead>
                    %id = -1
                    %id_puffer = 0
                    %for head in datatable[0]:
                        %if head.upper() == "ID":
                            %id=id_puffer
                        %end
                        <th>{{head}}</th>
                        %id_puffer += 1
                    %end
                    </thead>
                    %x = 0
                    %for col in datatable[1]:
                        
                        %y= x % 2
                        %if y > 0:
                            <tr>
                                %k = 0
                                %for i in col:
                                    %if id >= 0 and k == id:
                                        <td class="colored"><a href="{{path}}/{{i}}">{{i}}</a></td>
                                    %else:
                                        <td class="colored">{{i}}</td>
                                    %end
                                    %k+=1
                               %end
                            </tr>
                        %else:
                             <tr>
                                %k = 0
                                %for i in col:
                                    %if id >= 0 and k == id:
                                        <td><a href="{{path}}/{{i}}">{{i}}</a></td>
                                    %else:
                                        <td>{{i}}</td>
                                    %end
                                    %k+=1
                                %end
                            </tr> 
                        %end
                        %x+=1
                    %end
                    </table>