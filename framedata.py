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
character_json_directory_path = './resources/framedata/json/'


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
                move_json['frame']['recovery']),
            Recovery(move_json['recovery']['on_hit'],
                     move_json['recovery']['on_block']),
            Recovery(move_json['vt_cancel_recovery']['on_hit'],
                     move_json['vt_cancel_recovery']['on_block']),
            move_json['cancel_info'],
            move_json['damage'],
            move_json['stun'],
            move_json['meter_gain'],
            move_json['properties'],
            move_json['projectile_nullification'],
            move_json['airborne_hurtbox'],
            move_json['comments'])

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
        - meter_gain                {list(int)}     Meter gain of the move ( On_whiff, On_hit )
        - properties                {str}           Hit property of the move [ Throw, Low, Mid, Hight ]
        - projectile_nullification  {bool}          Move can nullify projectile
        - airborne_hurtbox          {str}           ???
        - comments                  {str}           Comments for the move
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
                 comments):
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


class Frame():
    """ Frame Structure
        - startup:  {int}   Number of startup frames
        - active:   {int}   Number of active frames
        - recovery: {int}   Number of recovery frames
    """

    def __init__(self, startup, active, recovery):
        self.startup = startup
        self.active = active
        self.recovery = recovery


class Recovery():
    """ Recovery Structure
        - on_hit    {str}   Number of frame on hit
        - on_block  {str}   Number of frame on block
    """

    def __init__(self, on_hit, on_block):
        self.on_hit = on_hit
        self.on_block = on_block


class MoveEncoder(json.JSONEncoder):
    """ Encode to JSON Move instance object """

    def default(self, obj):
        if isinstance(obj, Move):
            result = dict()
            result['type'] = obj.type
            result['name'] = obj.name
            result['frame'] = {'startup':   obj.frame.startup,
                               'active':    obj.frame.active,
                               'recovery':  obj.frame.recovery}
            result['recovery'] = {'on_hit':     obj.recovery.on_hit,
                                  'on_block':   obj.recovery.on_block}
            result['vt_cancel_recovery'] = {'on_hit':   obj.vt_cancel_recovery.on_hit,
                                            'on_block': obj.vt_cancel_recovery.on_block}
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
    name        = _get_name(move_tree)
    frame       = Frame(_get_frame_startup(move_tree),
                        _get_frame_active(move_tree),
                        _get_frame_recovery(move_tree))
    recovery    = Recovery(_get_recovery_on_hit(move_tree),
                           _get_recovery_on_block(move_tree))
    vtxrecovery = Recovery(_get_recovery_xvt_on_hit(move_tree),
                           _get_recovery_xvt_on_block(move_tree))
    cancel_info = _get_cancel_info(move_tree)
    damage      = _get_damage(move_tree)
    stun        = _get_stun(move_tree)
    meter_gain  = _get_meter_gain(move_tree)
    properties  = _get_properties(move_tree)
    proj_null   = _get_projectile_nullification(move_tree)
    airb_hurtbx = _get_airborn_hurtbox(move_tree)
    comments    = _get_comments(move_tree)

    return Move(move_type, name, frame, recovery, vtxrecovery, cancel_info,
                damage, stun, meter_gain, properties, proj_null, airb_hurtbx, comments)


def _get_general_data_init(move_tree, xpath):
    """ Private function to initialize most of captured data.
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        xpath:      {str} xpath for the capture
        Return:     {str|None} the string data captured or None if no data found
    """
    result = move_tree.xpath(xpath)
    if result != []:
        return ''.join(result)  # For have only one type of element to process -> str
    else:
        return None


def _get_name(move_tree):
    """ Private function extract the name of the move and return clean it
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {str} Name of the move
    """
    return _get_general_data_init(move_tree, './td[@class="name"]/p[@class="name"]/text()')


def _get_frame_startup(move_tree):
    """ Private function extract the frame startup data and return clean value
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {int|None} number of the startup frame for this move
    """
    raw_value = _get_general_data_init(move_tree, './td[2]/text()')
    if raw_value:
        match = re.match(r'\d+\+\d+', raw_value)    # '3+5'
        if match:
            return eval(match.group())              # -> 8

        match = re.match(r'\d+', raw_value)         # '5'
        if match:
            return int(match.group())               # -> 5
    else:
        return None


def _get_frame_active(move_tree):
    """ Private function extract the frame active data and return clean value
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {int|str|None} number of active frame for this move
    """
    raw_value = _get_general_data_init(move_tree, './td[3]/text()')
    if raw_value:
        if re.match(r'\d+×\d+', raw_value):                                # '13×3'
            return eval(re.sub(r'(\d+)×(\d+)', r'\1*\2', raw_value))       # -> 39

        match = re.search(r'\d+', raw_value)                               # '2' or '-/3'
        if match:
            return int(match.group())                                      # -> 2 or 3

        if re.match(r'\w+', raw_value):                                    # 'Until landing'
            return raw_value                                               # ->'Until landing'
    else:
        return None


def _get_frame_recovery(move_tree):
    """ Private function extract the frame active data and return clean value
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {int|None} number of recovery frame for this move
    """
    raw_value = _get_general_data_init(move_tree, './td[4]/text()')
    if raw_value:
        match = re.search(r'\d+\+\d+', raw_value)   # ['21+30 frame(s) after landing']
        if match:
            return eval(match.group())              # -> 51

        match = re.search(r'\d+', raw_value)        # '12'
        if match:
            return int(match.group())               # -> 12
    else:
        return None


def _get_recovery_on_hit(move_tree):
    """ Private function extract the number of recovery frame on hit
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {int|str|None} number of recovery frame on hit
    """
    raw_value = _get_general_data_init(move_tree, './td[5]/text()')
    if raw_value:
        match = re.match(r'\(\w+\)', raw_value)     # '(crumple)'
        if match:
            return match.group()                    # -> crumple

        if re.match(r'D', raw_value):               # 'D'
            return 'D'                              # -> D

        if re.match(r'\-$', raw_value):             # '-'
            return 0                                # -> 0

        if re.match(r'^±0', raw_value):             # '±0'
            return 0                                # -> 0

        match = re.match(r'\-*\d+', raw_value)      # '-3' or '7'
        if match:
            return int(match.group())               # -> -3 or 7
    else:
        return None


def _get_recovery_on_block(move_tree):
    """ Private function extract the number of recovery frame on block
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {int|str|None} number of recovery frame on block
    """
    raw_value = _get_general_data_init(move_tree, './td[6]/text()')
    if raw_value:
        if re.match(r'GB', raw_value):               # 'GB'
            return 'GB'                             # -> 'GB'

        if re.match(r'\-$', raw_value):             # '-'
            return 0                                # -> 0

        if re.match(r'^±0', raw_value):             # '±0'
            return 0                                # -> 0

        match = re.match(r'\-*\d+', raw_value)      # '-3' or '7'
        if match:
            return int(match.group())               # -> -3 or 7
    else:
        return None


def _get_recovery_xvt_on_hit(move_tree):
    """ Private function extract the number of recovery frame on V-trigger cancel on hit
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {int|str|None} number of recovery frame on V-trigger cancel on hit
    """
    raw_value = _get_general_data_init(move_tree, './td[7]/text()')
    if raw_value:
        if re.match(r'D', raw_value):                # 'D'
            return 'D'                              # -> 'D'

        match = re.match(r'\-*\d+', raw_value)      # '-3' or '7'
        if match:
            return int(match.group())               # -> -3 or 7
    else:
        return None


def _get_recovery_xvt_on_block(move_tree):
    """ Private function extract the number of recovery frame on V-trigger cancel on block
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {int|None} number of recovery frame on V-trigger cancel on block
    """
    raw_value = _get_general_data_init(move_tree, './td[8]/text()')
    if raw_value:
        if re.match(r'^\-\D*', raw_value):          # '-|-|-'
            return 0                                # -> 0

        match = re.match(r'\-*\d+', raw_value)      # '-3' or '7'
        if match:
            return int(match.group())               # -> -3 or 7
    else:
        return None


def _get_cancel_info(move_tree):
    """ Private function extract the cancel data and return value
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {list|None} cancel properties of the move
    """
    raw_value = move_tree.xpath('./td[9]/span/text()')

    if raw_value == []:
        return None
    else:
        return raw_value


def _get_damage(move_tree):
    """ Private function extract the damage of the move and return clean value
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {int|None} damage of the move
    """
    raw_value = _get_general_data_init(move_tree, './td[10]/span[@class="damageAll"]/text()')
    if raw_value:
        match = re.match(r'\d+\s?\+\s?\d+', raw_value)  # '70+90' or '100 + 50'
        if match:
            return eval(match.group())                  # -> 160 or 150

        match = re.match(r'\d+', raw_value)             # '70'
        if match:
            return int(match.group())                   # -> 70
    else:
        return None


def _get_stun(move_tree):
    """ Private function extract the stun of the move and return clean value
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {int|None} stun of the move
    """
    raw_value = _get_general_data_init(move_tree, './td[11]/span[@class="stunAll"]/text()')
    if raw_value:
        match = re.match(r'\d+\s?\+\s?\d+', raw_value)  # '70+90' or '100 + 50'
        if match:
            return eval(match.group())                  # -> 160 or 150

        match = re.match(r'\d+', raw_value)             # '70'
        if match:
            return int(match.group())                   # -> 70
    else:
        return None


def _get_meter_gain(move_tree):
    """ Private function extract the meter gain of the move and return clean value
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {list[2]} meter gain of the move
    """
    raw_value = _get_general_data_init(move_tree, './td[12]/text()')
    if raw_value:
        if '+' in raw_value:  # replace adition by the result !!!change raw_value!!!
            egal = r'{}'.format(eval(re.search(r'\d+\+\d+', raw_value).group()))  # return a raw string
            raw_value = re.sub(r'\d+\+\d+', egal, raw_value)

        if re.search(r'^\s+\d+\s+\/\s+\d+\s+', raw_value):      # ['\n\n                0 / 20            '] # noqa: E501
            temp_list = re.sub(r'.*(\-*\d+)\s+\/\s+(\d+).*$', r'\1,\2', raw_value).split(',')
            return [int(temp_list[0]), int(temp_list[1])]       # -> [10,20]
    else:
        return None


def _get_properties(move_tree):
    """ Private function extract the properties of the move and return it
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {str|None} properties of the move
    """
    return _get_general_data_init(move_tree, './td[13]/text()')


def _get_projectile_nullification(move_tree):
    """ Private function extract the projectile nullification properties of the move and return True or False
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {bool} projectile nullification properties of the move
    """
    raw_value = move_tree.xpath('./td[14]/text()')
    return True if raw_value != [] else False


def _get_airborn_hurtbox(move_tree):
    """ Private function extract the airborn hurtbox properties of the move and return it
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {str|None} airborn hurtbox properties of the move
    """
    return _get_general_data_init(move_tree, './td[15]/text()')


def _get_comments(move_tree):
    """ Private function extract the comments about the move and return it
        move_tree:  {lxml.html.HtmlElement} html element where you have all move information
        Return:     {list|None} comments about the move
    """
    raw_value = [move.strip() for move in move_tree.xpath(
        './td[@class="remarks"]/text()') if move.strip() != '']
    return raw_value if raw_value != [] else None


def _get_all_character_files(character_html_directory_path):
    return [character_html_directory_path + filepath for filepath in os.listdir(character_html_directory_path)
            if filepath.endswith('.html')]


def _load_all_character_from_html(character_html_directory_path):
    character_html_files = _get_all_character_files(character_html_directory_path)
    return [Framedata.loadFromHTML(filename) for filename in character_html_files]


def _save_all_character_to_json(all_character_framedata, character_json_directory_path):
    for framedata in all_character_framedata:
        framedata.saveToJSON('{}{}.json'.format(character_json_directory_path, framedata.character_name ))
    

# -[ Main ]-
if __name__ == '__main__':
    all_character_framedata = _load_all_character_from_html(character_html_directory_path)
    _save_all_character_to_json(all_character_framedata, character_json_directory_path)
