# This module extract frame data from official html file
# [STATE]   : POC ( Unfinished )
# [AUTHOR]  : bignos@gmail.com

# coding=utf-8

import sys              # for exit()
import os               # for path and basename
import lxml.html        # for parse XML
import re               # for Regular expression
import json             # for JSON dump and load

# -[ Data ]-
character_html_directory_path = './resources/framedata/html/'
# character_html_file_path = './resources/framedata/html/G.html'
# character_html_file_path = './resources/framedata/html/Ryu.html'

# character_json_file_path = './resources/framedata/json/G.json'

# -[ Class ]-


class Framedata():
    """ Framedata structure
        - character_name    {str}           Name of the character for this framedata
        - moves_vt1         {list(Move)}    Move list of the framedata for V-Trigger 1
        - moves_vt2         {list(Move)}    Move list of the framedata for V-Trigger 2
    """

    def __init__(self, character_name, moves_vt1, moves_vt2):
        self.character_name = character_name
        self.moves_vt1 = moves_vt1
        self.moves_vt2 = moves_vt2

    def __repr__(self):
        """ Return: {str}   String representation of Framedata instance """
        move_list_vt1 = ''.join(['{}'.format(move) for move in self.moves_vt1])
        move_list_vt2 = ''.join(['{}'.format(move) for move in self.moves_vt2])
        return """
Character name: {}
--------------------------------------------------------------------------------
move list VT1:
{}
--------------------------------------------------------------------------------
move list VT2:
{}
--------------------------------------------------------------------------------
        """.format(self.character_name, move_list_vt1, move_list_vt2)

    def loadFromJSON(path):
        """ Static method to build a framedata from a JSON file
            path:   {str}       Path of the JSON file
            Return: {Framedata} Framedata object with information of the JSON file
            Throw FileNotFoundError if the file in path is not found
            Throw PermissionError if you don't have permission to read the file
        """
        with open(path, 'r') as json_file:
            json_content = json.load(json_file)

        character_name = json_content['character_name']
        move_list_vt1 = list()
        move_list_vt2 = list()

        for move in json_content['moves_vt1']:
            move_list_vt1.append(Framedata._create_move_from_json_node(move))

        for move in json_content['moves_vt2']:
            move_list_vt2.append(Framedata._create_move_from_json_node(move))

        return Framedata(character_name, move_list_vt1, move_list_vt2)

    def _create_move_from_json_node(move_json):
        """ Private method to create a Move instance with a JSON move node
            move_json:  {dict}  The JSON node
            Return:     {Move}  The Move instance from the JSON node
        """
        return Move(
            move_json['type'],
            move_json['name'],
            Frame(
                move_json['frame']['startup'],
                move_json['frame']['active'],
                move_json['frame']['recovery'],
                clean=False),
            Recovery(move_json['recovery']['on_hit'],
                     move_json['recovery']['on_block'],
                     clean=False),
            Recovery(
                move_json['vt_cancel_recovery']['on_hit'],
                move_json['vt_cancel_recovery']['on_block'],
                clean=False),
            move_json['cancel_info'],
            move_json['damage'],
            move_json['stun'],
            move_json['meter_gain'],
            move_json['properties'],
            move_json['projectile_nullification'],
            move_json['airborne_hurtbox'],
            move_json['comments'],
            clean=False)

    def loadFromHTML(path):
        """ Static method to load a Framedata object from an HTML file
            path:   {str}       Path of the HTML file
            Return: {Framedata} Framedata from the HTML file
        """
        try:
            html_document = _read_html_file(path)
        except FileNotFoundError as exception:
            print('File not found: {}'.format(exception.filename))
            sys.exit()
        except PermissionError as exception:
            print('Permission denied: {}'.format(exception.filename))
            sys.exit()

        filename = os.path.basename(path)
        character_name = '.'.join(filename.split('.')[:-1])
        move_list_vt1 = _extract_data_from_tree(lxml.html.fromstring(html_document), 1)
        move_list_vt2 = _extract_data_from_tree(lxml.html.fromstring(html_document), 2)

        return Framedata(character_name, move_list_vt1, move_list_vt2)

    def saveToJSON(self, path):
        """ Save the framedata object to a JSON file
            path:   {str}   Path of the JSON file
            Return: None
        """
        with open(path, 'w') as json_file:
            json.dump(self, json_file, indent=4, separators=(',', ': '), sort_keys=True, cls=FramedataEncoder)


class Move():
    """ Move structure
        - type:                     {str}           Type of move [ Normal, Unique, Throws, V, Special, CA ]
        - name:                     {str}           Name of the move
        - frame:                    {Frame}         Frame informations of the move [ Startup, Active, Recovery ]
        - recovery:                 {Recovery}      Recovery informations of the move [ On_hit, On_block ]
        - vt_cancel_recovery:       {Recovery}      Recovery informations of the V-trigger cancel [ On_hit, On_block ]
        - cancel_info:              {list(str)}     Cancel properties of the move [ S, S*, CA, V, VS ]
        - damage:                   {int}           Damage of the move
        - stun:                     {int}           Stun of the move
        - meter_gain                {list(int)}    Meter gain of the move ( On_whiff, On_hit )
        - properties                {str}           Hit property of the move [ Throw, Low, Mid, Hight ]
        - projectile_nullification  {str}           Move can nullify projectile
        - airborne_hurtbox          {str}           ???
        - comments                  {str}           Comments for the move
        - clean                     {bool}          clean the data ( Yes / No )
    """

    def __init__(self,
                 move_type,
                 name,
                 frame,
                 recovery,
                 vt_cancel_recovery,
                 cancel_info,
                 damage,
                 stun,
                 meter_gain,
                 properties,
                 projectile_nullification,
                 airborne_hurtbox,
                 comments,
                 clean=True):
        self.type = move_type
        self.name = name
        self.frame = frame
        self.recovery = recovery
        self.vt_cancel_recovery = vt_cancel_recovery
        self.cancel_info = cancel_info
        self.damage = damage
        self.stun = stun
        self.meter_gain = meter_gain
        self.properties = properties
        self.projectile_nullification = projectile_nullification
        self.airborne_hurtbox = airborne_hurtbox
        self.comments = comments

        if clean:
            self._clean_attributes()

    def __repr__(self):
        """ Return: {str}   String representation of Move instance """
        format_str = """
    Name:                           {}
    Type:                           {}
    Frame startup:                  {}
    Frame active:                   {}
    Frame recovery:                 {}
    Recovery on hit:                {}
    Recovery on block:              {}
    VT cancel recovery on hit:      {}
    VT cancel recovery on block:    {}
    Cancel info:                    {}
    Damage:                         {}
    Stun:                           {}
    Meter gain:                     {}
    Properties:                     {}
    Projectile nullification:       {}
    Airborne hurtbox:               {}
    Comments:                       {}
        """
        return format_str.format(self.name,
                                 self.type,
                                 self.frame.startup,
                                 self.frame.active,
                                 self.frame.recovery,
                                 self.recovery.on_hit,
                                 self.recovery.on_block,
                                 self.vt_cancel_recovery.on_hit,
                                 self.vt_cancel_recovery.on_block,
                                 self.cancel_info,
                                 self.damage,
                                 self.stun,
                                 self.meter_gain,
                                 self.properties,
                                 self.projectile_nullification,
                                 self.airborne_hurtbox,
                                 self.comments)

    def _is_an_int(value):
        """ Return:  {bool}  True if value is an int else False """
        try:
            int(value)
            return True
        except ValueError:
            return False

    def _clean_attributes(self):
        """ Private method make to clean some attributes of the Move instance
            Clean:
                self.damage
                self.stun
                self.meter_gain
        """
        # self.damage
        if isinstance(self.damage, list):
            self.damage = [int(dam.replace(')', '')) for dam in self.damage if Move._is_an_int(dam.replace(')', ''))]
        else:
            try:
                self.damage = int(self.damage) if self.damage else None
            except ValueError:
                self.damage = eval(self.damage)

        # self.meter_gain
        if isinstance(self.meter_gain, list) and len(self.meter_gain) == 2:
            if Move._is_an_int(self.meter_gain[0].strip()):
                whiff_gain = int(self.meter_gain[0].strip())
            else:
                whiff_gain = int(re.sub(r'(\D+)(\d+)', r'\2', self.meter_gain[0]))
            if Move._is_an_int(self.meter_gain[1]):
                hit_gain = int(self.meter_gain[1])
            else:
                hit_gain = int(re.sub(r'(\D+)(\d+)', r'\2', self.meter_gain[1]))
            self.meter_gain = (whiff_gain, hit_gain)
        else:
            self.meter_gain = None

        # self.stun
        if isinstance(self.stun, list):
            self.stun = [int(stu.replace(')', '')) for stu in self.stun if Move._is_an_int(stu.replace(')', ''))]
        else:
            try:
                self.stun = int(self.stun) if self.stun else None
            except ValueError:
                self.stun = eval(self.stun)


class Frame():
    """ Frame Structure
        - startup:  {int}   Number of startup frames
        - active:   {int}   Number of active frames
        - recovery: {int}   Number of recovery frames
        - clean:    {bool}  Clean the data ( Yes / No )
    """

    def __init__(self, startup, active, recovery, clean=True):
        if clean:
            self._clean_attributes(startup, active, recovery)
        else:
            self.startup = startup
            self.active = active
            self.recovery = recovery

    def _clean_attributes(self, startup, active, recovery):
        """ Private method make to clean all attributes of the Frame instance """
        # startup
        self.startup = [self._clean_value(value) for value in startup] if isinstance(
            startup, list) else self._clean_value(startup)

        # active
        self.active = [self._clean_value(value) for value in active] if isinstance(
            active, list) else self._clean_value(active)

        # recovery
        self.recovery = [self._clean_value(value) for value in recovery] if isinstance(
            recovery, list) else self._clean_value(recovery)

    def _clean_value(self, value):
        result = None
        try:
            result = int(value)
        except (ValueError, TypeError):
            if isinstance(value, str):
                if '\u00d7' in value:
                    result = eval(value.replace('\u00d7', '*'))
                elif re.match(r'\d\+\d', value):
                    result = eval(re.sub(r'\D*(\d+\+\d+)\D*', r'\1', value))
                else:
                    pattern = r'\D*(\d+)\D*'
                    if re.match(pattern, value):
                        result = int(re.sub(pattern, r'\1', value))
                    else:
                        result = value

        return result


class Recovery():
    """ Recovery Structure
        - on_hit    {str}   Number of frame on hit
        - on_block  {str}   Number of frame on block
        - clean:    {bool}  Clean the data ( Yes / No )
    """

    def __init__(self, on_hit, on_block, clean=True):
        if clean:
            self._clean_attributes(on_hit, on_block)
        else:
            self.on_hit = on_hit
            self.on_block = on_block

    def _clean_attributes(self, on_hit, on_block):
        """ Private method make to clean all attributes of the Recovery instance """
        # on_hit
        self.on_hit = [self._clean_value(value) for value in on_hit] if isinstance(
            on_hit, list) else self._clean_value(on_hit)

        # on_block
        self.on_block = [self._clean_value(value) for value in on_block] if isinstance(
            on_block, list) else self._clean_value(on_block)

    def _clean_value(self, value):
        result = None
        try:
            result = int(value)
        except (ValueError, TypeError):
            if isinstance(value, str):
                if re.match(r'\D*', value):
                    result = value
                elif '/' in value:
                    result = [int(value) for value in self.on_block.split('/')]
                elif '\u00d7' in value:
                    result = eval(value.replace('\u00d7', '*'))
                elif re.match(r'\d\+\d', value):
                    result = eval(re.sub(r'\D*(\d+\+\d+)\D*', r'\1', value))
                else:
                    pattern = r'\D*(\d+)\D*'
                    if re.match(pattern, value):
                        result = int(re.sub(pattern, r'\1', value))
                    else:
                        result = value
        return result


class MoveEncoder(json.JSONEncoder):
    """ Encode to JSON Move instance object """

    def default(self, obj):
        if isinstance(obj, Move):
            result = dict()
            result['type'] = obj.type
            result['name'] = obj.name
            result['frame'] = {
                                'startup':      obj.frame.startup,
                                'active':       obj.frame.active,
                                'recovery':     obj.frame.recovery
                            }
            result['recovery'] = {
                                    'on_hit':       obj.recovery.on_hit,
                                    'on_block':     obj.recovery.on_block
                                }
            result['vt_cancel_recovery'] = {
                                                'on_hit':   obj.vt_cancel_recovery.on_hit,
                                                'on_block':   obj.vt_cancel_recovery.on_block
                                        }
            result['cancel_info'] = obj.cancel_info
            result['damage'] = obj.damage
            result['stun'] = obj.stun
            result['meter_gain'] = obj.meter_gain
            result['properties'] = obj.properties
            result['projectile_nullification'] = obj.projectile_nullification
            result['airborne_hurtbox'] = obj.airborne_hurtbox
            result['comments'] = obj.comments
            return result

        return json.JSONEncoder.default(self, obj)


class FramedataEncoder(MoveEncoder):
    """ Encode to JSON Framedata instance object """

    def default(self, obj):
        if isinstance(obj, Framedata):
            result = dict()
            result['character_name'] = obj.character_name
            result['moves_vt1'] = obj.moves_vt1
            result['moves_vt2'] = obj.moves_vt2
            return result

        return MoveEncoder.default(self, obj)

# -[ Private Function ]-


def _read_html_file(path):
    """ Private function read file and return content on a string
        path:   {str}   Path of the character file
        Return: {str}   The content of the file
        Throw FileNotFoundError if the file in path is not found
        Throw PermissionError if you don't have permission to read the file
    """
    with open(path, 'rt', encoding='utf-8') as document:
        result = document.read()
    return result


def _extract_data_from_tree(framedata_tree, vtrigger=1):
    """ Private function extract data from framedata tree and return a dict with strutured data
        framedata_tree: {lxml.html.HtmlElement} html framedata tree
        vtrigger:       {int}                   vtrigger move list, 1 or 2
        Return:         {list(Move)}
    """
    # Pre-condition
    assert isinstance(framedata_tree, lxml.html.HtmlElement), \
        'framedata_tree: {} is not a lxml.html.HtmlElement'.format(type(framedata_tree))
    assert vtrigger in (1, 2), \
        'vtrigger: {} is not 1 or 2'.format(vtrigger)

    result = list()

    # fill the move list
    for table in framedata_tree.xpath('//table[@class="frameTbl"][@vtrigger="{}"]'.format(vtrigger)):
        current_type = ''
        for tr in table.xpath('./tr'):
            current_type = tr.xpath('./th[@class="type"]/text()') or current_type

            if tr.xpath('./td') != []:
                result.append(_extract_move_from_tree(tr, current_type[0]))

    return result


def _extract_move_from_tree(move_tree, move_type):
    """ Private function extract all Move informations in the move tree
        move_tree: {lxml.html.HtmlElement} html element where you have all move information
        move_type: {str} Move type (You have to pass this parameter because is not in move_tree)
        Return: {Move} Move object with all data found in move_tree
    """
    name = move_tree.xpath('./td[@class="name"]/p[@class="name"]/text()')[0]

    frame = Frame(_sanityse(move_tree.xpath('./td[2]/text()')),
                  _sanityse(move_tree.xpath('./td[3]/text()')),
                  _sanityse(move_tree.xpath('./td[4]/text()')))
    recovery = Recovery(_sanityse(move_tree.xpath('./td[5]/text()')),
                        _sanityse(move_tree.xpath('./td[6]/text()')))
    vtxrecovery = Recovery(_sanityse(move_tree.xpath('./td[7]/text()')),
                           _sanityse(move_tree.xpath('./td[8]/text()')))
    cancel_info = _sanityse(move_tree.xpath('./td[9]/span/text()'))
    damage = _sanityse(move_tree.xpath('./td[10]/span[@class="damageAll"]/text()'))
    stun = _sanityse(move_tree.xpath('./td[11]/span[@class="stunAll"]/text()'))
    meter_gain = list(''.join(_sanityse(move_tree.xpath('./td[12]/text()'))).replace('\n', '').strip().split('/'))
    properties = _sanityse(move_tree.xpath('./td[13]/text()'))
    proj_null = _sanityse(move_tree.xpath('./td[14]/text()'))
    airb_hurtbx = _sanityse(move_tree.xpath('./td[15]/text()'))
    comments = _sanityse([move.strip() for move in move_tree.xpath(
        './td[@class="remarks"]/text()') if move.strip() != ''])

    return Move(move_type, name, frame, recovery, vtxrecovery, cancel_info,
                damage, stun, meter_gain, properties, proj_null, airb_hurtbx, comments)


def _get_frame_startup(move_tree):
    """ Private function extract the frame startup data and return clean value
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {int|None} number of the startup frame for this move
    """
    raw_value = move_tree.xpath('./td[2]/text()')

    if raw_value == []:
        return None

    raw_value = ''.join(raw_value) # For have only one type of element to process -> str

    if re.match(r'^\d+\+\d+', raw_value):
        return int(eval(re.sub(r'^(\d+\+\d+).*', '\1', raw_value)))

    if re.match(r'^\d+', raw_value):
        return int(re.sub(r'^(\d+)', '\1', raw_value))


def _get_frame_active(move_tree):
    """ Private function extract the frame active data and return clean value
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {int|str|None} number of active frame for this move
    """
    raw_value = move_tree.xpath('./td[3]/text()')

    if raw_value == []:
        return None

    raw_value = ''.join(raw_value)                                   # For have only one type of element to process -> str

    if re.match(r'\-\/\d+ ', raw_value):                             # ['-/3']
        return int(re.sub(r'.*(\d+)', '\1', raw_value))              # -> 3

    if re.match(r'\d+×\d+', raw_value):                              # ['13×3']
        return int(eval(re.sub(r'(\d+)×(\d+)', '\1*\2', raw_value))) # -> 39

    if re.match(r'^\d+', raw_value):
        return int(re.sub(r'^(\d+)', '\1', raw_value))

    if re.match(r'^\w+', raw_value):                                 # ['Until landing']
        return raw_value                                             # ->'Until landing'


def _get_frame_recovery(move_tree):
    """ Private function extract the frame active data and return clean value
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {int|str|None} number of recovery frame for this move
    """
    raw_value = move_tree.xpath('./td[4]/text()')

    if raw_value == []:
        return None

    raw_value = ''.join(raw_value)                                   # For have only one type of element to process -> str

    # TODO Make it
    if re.match(r'\-\/\d+ ', raw_value):                             # ['-/3']
        return int(re.sub(r'.*(\d+)', '\1', raw_value))              # -> 3

    if re.match(r'\d+×\d+', raw_value):                              # ['13×3']
        return int(eval(re.sub(r'(\d+)×(\d+)', '\1*\2', raw_value))) # -> 39

    if re.match(r'^\d+', raw_value):
        return int(re.sub(r'^(\d+)', '\1', raw_value))

    if re.match(r'^\w+', raw_value):                                 # ['Until landing']
        return raw_value                                             # ->'Until landing'


def _sanityse(value):
    """ Private function clean value.
        value:  {*} value to clean
        Return: {*} None if value is empty tuple or empty list
                    Element if value is a one tuple element or a one list element
                    value if value is already clean
    """
    if value == []:
        return None
    if len(value) == 1:
        return value[0]

    return value


def _get_all_character_files(character_html_directory_path):
    return [character_html_directory_path + filepath for filepath in os.listdir(character_html_directory_path)
            if filepath.endswith('.html')]


def _load_all_character_from_html(character_html_directory_path):
    character_html_files = _get_all_character_files(character_html_directory_path)
    return [Framedata.loadFromHTML(filename) for filename in character_html_files]


# -[ Main ]-
if __name__ == '__main__':
    # framedata = Framedata.loadFromHTML( character_html_file_path )
    # framedata.saveToJSON( character_json_file_path )
    # framedata = Framedata.loadFromJSON( character_json_file_path )
    # print( framedata )
    _load_all_character_from_html(character_html_directory_path)
