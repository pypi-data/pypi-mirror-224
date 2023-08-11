# coding: UTF-8
import sys
bstack1l1l11l11_opy_ = sys.version_info [0] == 2
bstack1llll1ll1_opy_ = 2048
bstack11ll1llll_opy_ = 7
def bstack111lll1l1_opy_ (bstack1l11ll1l_opy_):
    global bstack1l1ll111l_opy_
    stringNr = ord (bstack1l11ll1l_opy_ [-1])
    bstack1l1l1111_opy_ = bstack1l11ll1l_opy_ [:-1]
    bstack11ll1lll_opy_ = stringNr % len (bstack1l1l1111_opy_)
    bstack1l1111lll_opy_ = bstack1l1l1111_opy_ [:bstack11ll1lll_opy_] + bstack1l1l1111_opy_ [bstack11ll1lll_opy_:]
    if bstack1l1l11l11_opy_:
        bstack1ll1l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1llll1ll1_opy_ - (bstack1l1lll1l1_opy_ + stringNr) % bstack11ll1llll_opy_) for bstack1l1lll1l1_opy_, char in enumerate (bstack1l1111lll_opy_)])
    else:
        bstack1ll1l1ll_opy_ = str () .join ([chr (ord (char) - bstack1llll1ll1_opy_ - (bstack1l1lll1l1_opy_ + stringNr) % bstack11ll1llll_opy_) for bstack1l1lll1l1_opy_, char in enumerate (bstack1l1111lll_opy_)])
    return eval (bstack1ll1l1ll_opy_)
import atexit
import os
import signal
import sys
import time
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
from multiprocessing import Pool
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
bstack11lll111_opy_ = {
	bstack111lll1l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ࠀ"): bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡳࠩࠁ"),
  bstack111lll1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩࠂ"): bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡫ࡦࡻࠪࠃ"),
  bstack111lll1l1_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫࠄ"): bstack111lll1l1_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ࠅ"),
  bstack111lll1l1_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪࠆ"): bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫࡟ࡸ࠵ࡦࠫࠇ"),
  bstack111lll1l1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪࠈ"): bstack111lll1l1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࠧࠉ"),
  bstack111lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪࠊ"): bstack111lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࠧࠋ"),
  bstack111lll1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧࠌ"): bstack111lll1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨࠍ"),
  bstack111lll1l1_opy_ (u"ࠫࡩ࡫ࡢࡶࡩࠪࠎ"): bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩࠪࠏ"),
  bstack111lll1l1_opy_ (u"࠭ࡣࡰࡰࡶࡳࡱ࡫ࡌࡰࡩࡶࠫࠐ"): bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡶࡳࡱ࡫ࠧࠑ"),
  bstack111lll1l1_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭ࠒ"): bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭ࠓ"),
  bstack111lll1l1_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧࠔ"): bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧࠕ"),
  bstack111lll1l1_opy_ (u"ࠬࡼࡩࡥࡧࡲࠫࠖ"): bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡼࡩࡥࡧࡲࠫࠗ"),
  bstack111lll1l1_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭࠘"): bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭࠙"),
  bstack111lll1l1_opy_ (u"ࠩࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩࠚ"): bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩࠛ"),
  bstack111lll1l1_opy_ (u"ࠫ࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩࠜ"): bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩࠝ"),
  bstack111lll1l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨࠞ"): bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨࠟ"),
  bstack111lll1l1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪࠠ"): bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫࠡ"),
  bstack111lll1l1_opy_ (u"ࠪࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩࠢ"): bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩࠣ"),
  bstack111lll1l1_opy_ (u"ࠬ࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪࠤ"): bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪࠥ"),
  bstack111lll1l1_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧࠦ"): bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧࠧ"),
  bstack111lll1l1_opy_ (u"ࠩࡶࡩࡳࡪࡋࡦࡻࡶࠫࠨ"): bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡶࡩࡳࡪࡋࡦࡻࡶࠫࠩ"),
  bstack111lll1l1_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭ࠪ"): bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭ࠫ"),
  bstack111lll1l1_opy_ (u"࠭ࡨࡰࡵࡷࡷࠬࠬ"): bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡨࡰࡵࡷࡷࠬ࠭"),
  bstack111lll1l1_opy_ (u"ࠨࡤࡩࡧࡦࡩࡨࡦࠩ࠮"): bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡩࡧࡦࡩࡨࡦࠩ࠯"),
  bstack111lll1l1_opy_ (u"ࠪࡻࡸࡒ࡯ࡤࡣ࡯ࡗࡺࡶࡰࡰࡴࡷࠫ࠰"): bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡻࡸࡒ࡯ࡤࡣ࡯ࡗࡺࡶࡰࡰࡴࡷࠫ࠱"),
  bstack111lll1l1_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ࠲"): bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ࠳"),
  bstack111lll1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ࠴"): bstack111lll1l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ࠵"),
  bstack111lll1l1_opy_ (u"ࠩࡵࡩࡦࡲࡍࡰࡤ࡬ࡰࡪ࠭࠶"): bstack111lll1l1_opy_ (u"ࠪࡶࡪࡧ࡬ࡠ࡯ࡲࡦ࡮ࡲࡥࠨ࠷"),
  bstack111lll1l1_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ࠸"): bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡶࡰࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ࠹"),
  bstack111lll1l1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭࠺"): bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭࠻"),
  bstack111lll1l1_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩ࠼"): bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩ࠽"),
  bstack111lll1l1_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡌࡲࡸ࡫ࡣࡶࡴࡨࡇࡪࡸࡴࡴࠩ࠾"): bstack111lll1l1_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡗࡸࡲࡃࡦࡴࡷࡷࠬ࠿"),
  bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧࡀ"): bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧࡁ"),
  bstack111lll1l1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧࡂ"): bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡱࡸࡶࡨ࡫ࠧࡃ"),
  bstack111lll1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࡄ"): bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࡅ"),
  bstack111lll1l1_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ࡆ"): bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ࡇ"),
}
bstack1lll1l1l_opy_ = [
  bstack111lll1l1_opy_ (u"࠭࡯ࡴࠩࡈ"),
  bstack111lll1l1_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪࡉ"),
  bstack111lll1l1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪࡊ"),
  bstack111lll1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧࡋ"),
  bstack111lll1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧࡌ"),
  bstack111lll1l1_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨࡍ"),
  bstack111lll1l1_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬࡎ"),
]
bstack1l11111l1_opy_ = {
  bstack111lll1l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨࡏ"): [bstack111lll1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨࡐ"), bstack111lll1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡤࡔࡁࡎࡇࠪࡑ")],
  bstack111lll1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬࡒ"): bstack111lll1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭ࡓ"),
  bstack111lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧࡔ"): bstack111lll1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡒࡆࡓࡅࠨࡕ"),
  bstack111lll1l1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫࡖ"): bstack111lll1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠬࡗ"),
  bstack111lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࡘ"): bstack111lll1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕ࡙ࠫ"),
  bstack111lll1l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯࡚ࠪ"): bstack111lll1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡆࡘࡁࡍࡎࡈࡐࡘࡥࡐࡆࡔࡢࡔࡑࡇࡔࡇࡑࡕࡑ࡛ࠬ"),
  bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ࡜"): bstack111lll1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࠫ࡝"),
  bstack111lll1l1_opy_ (u"ࠧࡳࡧࡵࡹࡳ࡚ࡥࡴࡶࡶࠫ࡞"): bstack111lll1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬ࡟"),
  bstack111lll1l1_opy_ (u"ࠩࡤࡴࡵ࠭ࡠ"): [bstack111lll1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡔࡕࡥࡉࡅࠩࡡ"), bstack111lll1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡕࡖࠧࡢ")],
  bstack111lll1l1_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧࡣ"): bstack111lll1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡕࡂࡔࡇࡕ࡚ࡆࡈࡉࡍࡋࡗ࡝ࡤࡊࡅࡃࡗࡊࠫࡤ"),
  bstack111lll1l1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫࡥ"): bstack111lll1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫࡦ")
}
bstack1_opy_ = {
  bstack111lll1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫࡧ"): [bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡸ࡟࡯ࡣࡰࡩࠬࡨ"), bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡲࡏࡣࡰࡩࠬࡩ")],
  bstack111lll1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨࡪ"): [bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷࡤࡱࡥࡺࠩ࡫"), bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ࡬")],
  bstack111lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ࡭"): bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ࡮"),
  bstack111lll1l1_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨ࡯"): bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨࡰ"),
  bstack111lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࡱ"): bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࡲ"),
  bstack111lll1l1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧࡳ"): [bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡱࡲࡳࠫࡴ"), bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨࡵ")],
  bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧࡶ"): bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࠩࡷ"),
  bstack111lll1l1_opy_ (u"ࠬࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩࡸ"): bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩࡹ"),
  bstack111lll1l1_opy_ (u"ࠧࡢࡲࡳࠫࡺ"): bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡲࡳࠫࡻ"),
  bstack111lll1l1_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫࡼ"): bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫࡽ"),
  bstack111lll1l1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨࡾ"): bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨࡿ")
}
bstack1l11ll1l1_opy_ = {
  bstack111lll1l1_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩࢀ"): bstack111lll1l1_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫࢁ"),
  bstack111lll1l1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪࢂ"): [bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫࢃ"), bstack111lll1l1_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ࢄ")],
  bstack111lll1l1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩࢅ"): bstack111lll1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪࢆ"),
  bstack111lll1l1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪࢇ"): bstack111lll1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ࢈"),
  bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ࢉ"): [bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪࢊ"), bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩࢋ")],
  bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬࢌ"): bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧࢍ"),
  bstack111lll1l1_opy_ (u"࠭ࡲࡦࡣ࡯ࡑࡴࡨࡩ࡭ࡧࠪࢎ"): bstack111lll1l1_opy_ (u"ࠧࡳࡧࡤࡰࡤࡳ࡯ࡣ࡫࡯ࡩࠬ࢏"),
  bstack111lll1l1_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ࢐"): [bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡳࡴ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ࢑"), bstack111lll1l1_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫ࢒")],
  bstack111lll1l1_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡍࡳࡹࡥࡤࡷࡵࡩࡈ࡫ࡲࡵࡵࠪ࢓"): [bstack111lll1l1_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡘࡹ࡬ࡄࡧࡵࡸࡸ࠭࢔"), bstack111lll1l1_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹ࡙ࡳ࡭ࡅࡨࡶࡹ࠭࢕")]
}
bstack1l111111_opy_ = [
  bstack111lll1l1_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭࢖"),
  bstack111lll1l1_opy_ (u"ࠨࡲࡤ࡫ࡪࡒ࡯ࡢࡦࡖࡸࡷࡧࡴࡦࡩࡼࠫࢗ"),
  bstack111lll1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨ࢘"),
  bstack111lll1l1_opy_ (u"ࠪࡷࡪࡺࡗࡪࡰࡧࡳࡼࡘࡥࡤࡶ࢙ࠪ"),
  bstack111lll1l1_opy_ (u"ࠫࡹ࡯࡭ࡦࡱࡸࡸࡸ࢚࠭"),
  bstack111lll1l1_opy_ (u"ࠬࡹࡴࡳ࡫ࡦࡸࡋ࡯࡬ࡦࡋࡱࡸࡪࡸࡡࡤࡶࡤࡦ࡮ࡲࡩࡵࡻ࢛ࠪ"),
  bstack111lll1l1_opy_ (u"࠭ࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࡒࡵࡳࡲࡶࡴࡃࡧ࡫ࡥࡻ࡯࡯ࡳࠩ࢜"),
  bstack111lll1l1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ࢝"),
  bstack111lll1l1_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭࢞"),
  bstack111lll1l1_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ࢟"),
  bstack111lll1l1_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩࢠ"),
  bstack111lll1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬࢡ"),
]
bstack1l111l1l1_opy_ = [
  bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩࢢ"),
  bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢣ"),
  bstack111lll1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢤ"),
  bstack111lll1l1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨࢥ"),
  bstack111lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬࢦ"),
  bstack111lll1l1_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬࢧ"),
  bstack111lll1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧࢨ"),
  bstack111lll1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩࢩ"),
  bstack111lll1l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩࢪ"),
  bstack111lll1l1_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬࢫ")
]
bstack1lll1lll1_opy_ = [
  bstack111lll1l1_opy_ (u"ࠨࡷࡳࡰࡴࡧࡤࡎࡧࡧ࡭ࡦ࠭ࢬ"),
  bstack111lll1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫࢭ"),
  bstack111lll1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ࢮ"),
  bstack111lll1l1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩࢯ"),
  bstack111lll1l1_opy_ (u"ࠬࡺࡥࡴࡶࡓࡶ࡮ࡵࡲࡪࡶࡼࠫࢰ"),
  bstack111lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩࢱ"),
  bstack111lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩ࡚ࡡࡨࠩࢲ"),
  bstack111lll1l1_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ࢳ"),
  bstack111lll1l1_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫࢴ"),
  bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨࢵ"),
  bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬࢶ"),
  bstack111lll1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫࢷ"),
  bstack111lll1l1_opy_ (u"࠭࡯ࡴࠩࢸ"),
  bstack111lll1l1_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪࢹ"),
  bstack111lll1l1_opy_ (u"ࠨࡪࡲࡷࡹࡹࠧࢺ"),
  bstack111lll1l1_opy_ (u"ࠩࡤࡹࡹࡵࡗࡢ࡫ࡷࠫࢻ"),
  bstack111lll1l1_opy_ (u"ࠪࡶࡪ࡭ࡩࡰࡰࠪࢼ"),
  bstack111lll1l1_opy_ (u"ࠫࡹ࡯࡭ࡦࡼࡲࡲࡪ࠭ࢽ"),
  bstack111lll1l1_opy_ (u"ࠬࡳࡡࡤࡪ࡬ࡲࡪ࠭ࢾ"),
  bstack111lll1l1_opy_ (u"࠭ࡲࡦࡵࡲࡰࡺࡺࡩࡰࡰࠪࢿ"),
  bstack111lll1l1_opy_ (u"ࠧࡪࡦ࡯ࡩ࡙࡯࡭ࡦࡱࡸࡸࠬࣀ"),
  bstack111lll1l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡐࡴ࡬ࡩࡳࡺࡡࡵ࡫ࡲࡲࠬࣁ"),
  bstack111lll1l1_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࠨࣂ"),
  bstack111lll1l1_opy_ (u"ࠪࡲࡴࡖࡡࡨࡧࡏࡳࡦࡪࡔࡪ࡯ࡨࡳࡺࡺࠧࣃ"),
  bstack111lll1l1_opy_ (u"ࠫࡧ࡬ࡣࡢࡥ࡫ࡩࠬࣄ"),
  bstack111lll1l1_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫࣅ"),
  bstack111lll1l1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡙ࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪࣆ"),
  bstack111lll1l1_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡓࡦࡰࡧࡏࡪࡿࡳࠨࣇ"),
  bstack111lll1l1_opy_ (u"ࠨࡴࡨࡥࡱࡓ࡯ࡣ࡫࡯ࡩࠬࣈ"),
  bstack111lll1l1_opy_ (u"ࠩࡱࡳࡕ࡯ࡰࡦ࡮࡬ࡲࡪ࠭ࣉ"),
  bstack111lll1l1_opy_ (u"ࠪࡧ࡭࡫ࡣ࡬ࡗࡕࡐࠬ࣊"),
  bstack111lll1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣋"),
  bstack111lll1l1_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡈࡵ࡯࡬࡫ࡨࡷࠬ࣌"),
  bstack111lll1l1_opy_ (u"࠭ࡣࡢࡲࡷࡹࡷ࡫ࡃࡳࡣࡶ࡬ࠬ࣍"),
  bstack111lll1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ࣎"),
  bstack111lll1l1_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ࣏"),
  bstack111lll1l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࡜ࡥࡳࡵ࡬ࡳࡳ࣐࠭"),
  bstack111lll1l1_opy_ (u"ࠪࡲࡴࡈ࡬ࡢࡰ࡮ࡔࡴࡲ࡬ࡪࡰࡪ࣑ࠫ"),
  bstack111lll1l1_opy_ (u"ࠫࡲࡧࡳ࡬ࡕࡨࡲࡩࡑࡥࡺࡵ࣒ࠪ"),
  bstack111lll1l1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡑࡵࡧࡴ࣓ࠩ"),
  bstack111lll1l1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡏࡤࠨࣔ"),
  bstack111lll1l1_opy_ (u"ࠧࡥࡧࡧ࡭ࡨࡧࡴࡦࡦࡇࡩࡻ࡯ࡣࡦࠩࣕ"),
  bstack111lll1l1_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡑࡣࡵࡥࡲࡹࠧࣖ"),
  bstack111lll1l1_opy_ (u"ࠩࡳ࡬ࡴࡴࡥࡏࡷࡰࡦࡪࡸࠧࣗ"),
  bstack111lll1l1_opy_ (u"ࠪࡲࡪࡺࡷࡰࡴ࡮ࡐࡴ࡭ࡳࠨࣘ"),
  bstack111lll1l1_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࡑࡳࡸ࡮ࡵ࡮ࡴࠩࣙ"),
  bstack111lll1l1_opy_ (u"ࠬࡩ࡯࡯ࡵࡲࡰࡪࡒ࡯ࡨࡵࠪࣚ"),
  bstack111lll1l1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ࣛ"),
  bstack111lll1l1_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫࣜ"),
  bstack111lll1l1_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡃ࡫ࡲࡱࡪࡺࡲࡪࡥࠪࣝ"),
  bstack111lll1l1_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࡗ࠴ࠪࣞ"),
  bstack111lll1l1_opy_ (u"ࠪࡱ࡮ࡪࡓࡦࡵࡶ࡭ࡴࡴࡉ࡯ࡵࡷࡥࡱࡲࡁࡱࡲࡶࠫࣟ"),
  bstack111lll1l1_opy_ (u"ࠫࡪࡹࡰࡳࡧࡶࡷࡴ࡙ࡥࡳࡸࡨࡶࠬ࣠"),
  bstack111lll1l1_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡌࡰࡩࡶࠫ࣡"),
  bstack111lll1l1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡄࡦࡳࠫ࣢"),
  bstack111lll1l1_opy_ (u"ࠧࡵࡧ࡯ࡩࡲ࡫ࡴࡳࡻࡏࡳ࡬ࡹࣣࠧ"),
  bstack111lll1l1_opy_ (u"ࠨࡵࡼࡲࡨ࡚ࡩ࡮ࡧ࡚࡭ࡹ࡮ࡎࡕࡒࠪࣤ"),
  bstack111lll1l1_opy_ (u"ࠩࡪࡩࡴࡒ࡯ࡤࡣࡷ࡭ࡴࡴࠧࣥ"),
  bstack111lll1l1_opy_ (u"ࠪ࡫ࡵࡹࡌࡰࡥࡤࡸ࡮ࡵ࡮ࠨࣦ"),
  bstack111lll1l1_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡕࡸ࡯ࡧ࡫࡯ࡩࠬࣧ"),
  bstack111lll1l1_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡓ࡫ࡴࡸࡱࡵ࡯ࠬࣨ"),
  bstack111lll1l1_opy_ (u"࠭ࡦࡰࡴࡦࡩࡈ࡮ࡡ࡯ࡩࡨࡎࡦࡸࣩࠧ"),
  bstack111lll1l1_opy_ (u"ࠧࡹ࡯ࡶࡎࡦࡸࠧ࣪"),
  bstack111lll1l1_opy_ (u"ࠨࡺࡰࡼࡏࡧࡲࠨ࣫"),
  bstack111lll1l1_opy_ (u"ࠩࡰࡥࡸࡱࡃࡰ࡯ࡰࡥࡳࡪࡳࠨ࣬"),
  bstack111lll1l1_opy_ (u"ࠪࡱࡦࡹ࡫ࡃࡣࡶ࡭ࡨࡇࡵࡵࡪ࣭ࠪ"),
  bstack111lll1l1_opy_ (u"ࠫࡼࡹࡌࡰࡥࡤࡰࡘࡻࡰࡱࡱࡵࡸ࣮ࠬ"),
  bstack111lll1l1_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ࣯"),
  bstack111lll1l1_opy_ (u"࠭ࡡࡱࡲ࡙ࡩࡷࡹࡩࡰࡰࣰࠪ"),
  bstack111lll1l1_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸࣱ࠭"),
  bstack111lll1l1_opy_ (u"ࠨࡴࡨࡷ࡮࡭࡮ࡂࡲࡳࣲࠫ"),
  bstack111lll1l1_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡲ࡮ࡳࡡࡵ࡫ࡲࡲࡸ࠭ࣳ"),
  bstack111lll1l1_opy_ (u"ࠪࡧࡦࡴࡡࡳࡻࠪࣴ"),
  bstack111lll1l1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬࣵ"),
  bstack111lll1l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࣶࠬ"),
  bstack111lll1l1_opy_ (u"࠭ࡩࡦࠩࣷ"),
  bstack111lll1l1_opy_ (u"ࠧࡦࡦࡪࡩࠬࣸ"),
  bstack111lll1l1_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨࣹ"),
  bstack111lll1l1_opy_ (u"ࠩࡴࡹࡪࡻࡥࠨࣺ"),
  bstack111lll1l1_opy_ (u"ࠪ࡭ࡳࡺࡥࡳࡰࡤࡰࠬࣻ"),
  bstack111lll1l1_opy_ (u"ࠫࡦࡶࡰࡔࡶࡲࡶࡪࡉ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠬࣼ"),
  bstack111lll1l1_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡈࡧ࡭ࡦࡴࡤࡍࡲࡧࡧࡦࡋࡱ࡮ࡪࡩࡴࡪࡱࡱࠫࣽ"),
  bstack111lll1l1_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡌࡰࡩࡶࡉࡽࡩ࡬ࡶࡦࡨࡌࡴࡹࡴࡴࠩࣾ"),
  bstack111lll1l1_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࡎࡴࡣ࡭ࡷࡧࡩࡍࡵࡳࡵࡵࠪࣿ"),
  bstack111lll1l1_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡂࡲࡳࡗࡪࡺࡴࡪࡰࡪࡷࠬऀ"),
  bstack111lll1l1_opy_ (u"ࠩࡵࡩࡸ࡫ࡲࡷࡧࡇࡩࡻ࡯ࡣࡦࠩँ"),
  bstack111lll1l1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪं"),
  bstack111lll1l1_opy_ (u"ࠫࡸ࡫࡮ࡥࡍࡨࡽࡸ࠭ः"),
  bstack111lll1l1_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡕࡧࡳࡴࡥࡲࡨࡪ࠭ऄ"),
  bstack111lll1l1_opy_ (u"࠭ࡵࡱࡦࡤࡸࡪࡏ࡯ࡴࡆࡨࡺ࡮ࡩࡥࡔࡧࡷࡸ࡮ࡴࡧࡴࠩअ"),
  bstack111lll1l1_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡁࡶࡦ࡬ࡳࡎࡴࡪࡦࡥࡷ࡭ࡴࡴࠧआ"),
  bstack111lll1l1_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡂࡲࡳࡰࡪࡖࡡࡺࠩइ"),
  bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪई"),
  bstack111lll1l1_opy_ (u"ࠪࡻࡩ࡯࡯ࡔࡧࡵࡺ࡮ࡩࡥࠨउ"),
  bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ऊ"),
  bstack111lll1l1_opy_ (u"ࠬࡶࡲࡦࡸࡨࡲࡹࡉࡲࡰࡵࡶࡗ࡮ࡺࡥࡕࡴࡤࡧࡰ࡯࡮ࡨࠩऋ"),
  bstack111lll1l1_opy_ (u"࠭ࡨࡪࡩ࡫ࡇࡴࡴࡴࡳࡣࡶࡸࠬऌ"),
  bstack111lll1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡐࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࡶࠫऍ"),
  bstack111lll1l1_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡔ࡫ࡰࠫऎ"),
  bstack111lll1l1_opy_ (u"ࠩࡶ࡭ࡲࡕࡰࡵ࡫ࡲࡲࡸ࠭ए"),
  bstack111lll1l1_opy_ (u"ࠪࡶࡪࡳ࡯ࡷࡧࡌࡓࡘࡇࡰࡱࡕࡨࡸࡹ࡯࡮ࡨࡵࡏࡳࡨࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠨऐ"),
  bstack111lll1l1_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ऑ"),
  bstack111lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧऒ"),
  bstack111lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠨओ"),
  bstack111lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭औ"),
  bstack111lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪक"),
  bstack111lll1l1_opy_ (u"ࠩࡳࡥ࡬࡫ࡌࡰࡣࡧࡗࡹࡸࡡࡵࡧࡪࡽࠬख"),
  bstack111lll1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩग"),
  bstack111lll1l1_opy_ (u"ࠫࡹ࡯࡭ࡦࡱࡸࡸࡸ࠭घ"),
  bstack111lll1l1_opy_ (u"ࠬࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡑࡴࡲࡱࡵࡺࡂࡦࡪࡤࡺ࡮ࡵࡲࠨङ")
]
bstack111ll1l1l_opy_ = {
  bstack111lll1l1_opy_ (u"࠭ࡶࠨच"): bstack111lll1l1_opy_ (u"ࠧࡷࠩछ"),
  bstack111lll1l1_opy_ (u"ࠨࡨࠪज"): bstack111lll1l1_opy_ (u"ࠩࡩࠫझ"),
  bstack111lll1l1_opy_ (u"ࠪࡪࡴࡸࡣࡦࠩञ"): bstack111lll1l1_opy_ (u"ࠫ࡫ࡵࡲࡤࡧࠪट"),
  bstack111lll1l1_opy_ (u"ࠬࡵ࡮࡭ࡻࡤࡹࡹࡵ࡭ࡢࡶࡨࠫठ"): bstack111lll1l1_opy_ (u"࠭࡯࡯࡮ࡼࡅࡺࡺ࡯࡮ࡣࡷࡩࠬड"),
  bstack111lll1l1_opy_ (u"ࠧࡧࡱࡵࡧࡪࡲ࡯ࡤࡣ࡯ࠫढ"): bstack111lll1l1_opy_ (u"ࠨࡨࡲࡶࡨ࡫࡬ࡰࡥࡤࡰࠬण"),
  bstack111lll1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡩࡱࡶࡸࠬत"): bstack111lll1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭थ"),
  bstack111lll1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡳࡳࡷࡺࠧद"): bstack111lll1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡴࡸࡴࠨध"),
  bstack111lll1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࡺࡹࡥࡳࠩन"): bstack111lll1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪऩ"),
  bstack111lll1l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡰࡢࡵࡶࠫप"): bstack111lll1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬफ"),
  bstack111lll1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡨࡰࡵࡷࠫब"): bstack111lll1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡉࡱࡶࡸࠬभ"),
  bstack111lll1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡲࡲࡶࡹ࠭म"): bstack111lll1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡳࡷࡺࠧय"),
  bstack111lll1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡹࡸ࡫ࡲࠨर"): bstack111lll1l1_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾ࡛ࡳࡦࡴࠪऱ"),
  bstack111lll1l1_opy_ (u"ࠩ࠰ࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡵࡴࡧࡵࠫल"): bstack111lll1l1_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡖࡵࡨࡶࠬळ"),
  bstack111lll1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡱࡣࡶࡷࠬऴ"): bstack111lll1l1_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡥࡸࡹࠧव"),
  bstack111lll1l1_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡴࡦࡹࡳࠨश"): bstack111lll1l1_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽࡕࡧࡳࡴࠩष"),
  bstack111lll1l1_opy_ (u"ࠨࡤ࡬ࡲࡦࡸࡹࡱࡣࡷ࡬ࠬस"): bstack111lll1l1_opy_ (u"ࠩࡥ࡭ࡳࡧࡲࡺࡲࡤࡸ࡭࠭ह"),
  bstack111lll1l1_opy_ (u"ࠪࡴࡦࡩࡦࡪ࡮ࡨࠫऺ"): bstack111lll1l1_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧऻ"),
  bstack111lll1l1_opy_ (u"ࠬࡶࡡࡤ࠯ࡩ࡭ࡱ࡫़ࠧ"): bstack111lll1l1_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩऽ"),
  bstack111lll1l1_opy_ (u"ࠧ࠮ࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪा"): bstack111lll1l1_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫि"),
  bstack111lll1l1_opy_ (u"ࠩ࡯ࡳ࡬࡬ࡩ࡭ࡧࠪी"): bstack111lll1l1_opy_ (u"ࠪࡰࡴ࡭ࡦࡪ࡮ࡨࠫु"),
  bstack111lll1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ू"): bstack111lll1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧृ"),
}
bstack1l1l1ll1l_opy_ = bstack111lll1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡩࡷࡥ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡸࡦ࠲࡬ࡺࡨࠧॄ")
bstack1l1111l_opy_ = bstack111lll1l1_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯ࡩࡷࡥ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠪॅ")
bstack1ll1lll11_opy_ = bstack111lll1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱࡫ࡹࡧ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡱࡩࡽࡺ࡟ࡩࡷࡥࡷࠬॆ")
bstack11lll1ll_opy_ = {
  bstack111lll1l1_opy_ (u"ࠩࡦࡶ࡮ࡺࡩࡤࡣ࡯ࠫे"): 50,
  bstack111lll1l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩै"): 40,
  bstack111lll1l1_opy_ (u"ࠫࡼࡧࡲ࡯࡫ࡱ࡫ࠬॉ"): 30,
  bstack111lll1l1_opy_ (u"ࠬ࡯࡮ࡧࡱࠪॊ"): 20,
  bstack111lll1l1_opy_ (u"࠭ࡤࡦࡤࡸ࡫ࠬो"): 10
}
bstack11l111l1_opy_ = bstack11lll1ll_opy_[bstack111lll1l1_opy_ (u"ࠧࡪࡰࡩࡳࠬौ")]
bstack11ll1l1ll_opy_ = bstack111lll1l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵्ࠧ")
bstack111lllll_opy_ = bstack111lll1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࠧॎ")
bstack11l111ll_opy_ = bstack111lll1l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࠩॏ")
bstack1l1l11l1_opy_ = bstack111lll1l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࠪॐ")
bstack1l11lll11_opy_ = [bstack111lll1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭॑"), bstack111lll1l1_opy_ (u"࡙࠭ࡐࡗࡕࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ॒࠭")]
bstack1ll1ll111_opy_ = [bstack111lll1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪ॓"), bstack111lll1l1_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪ॔")]
bstack11111l11_opy_ = [
  bstack111lll1l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡔࡡ࡮ࡧࠪॕ"),
  bstack111lll1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬॖ"),
  bstack111lll1l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨॗ"),
  bstack111lll1l1_opy_ (u"ࠬࡴࡥࡸࡅࡲࡱࡲࡧ࡮ࡥࡖ࡬ࡱࡪࡵࡵࡵࠩक़"),
  bstack111lll1l1_opy_ (u"࠭ࡡࡱࡲࠪख़"),
  bstack111lll1l1_opy_ (u"ࠧࡶࡦ࡬ࡨࠬग़"),
  bstack111lll1l1_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪज़"),
  bstack111lll1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡦࠩड़"),
  bstack111lll1l1_opy_ (u"ࠪࡳࡷ࡯ࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠨढ़"),
  bstack111lll1l1_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡨࡦࡻ࡯ࡥࡸࠩफ़"),
  bstack111lll1l1_opy_ (u"ࠬࡴ࡯ࡓࡧࡶࡩࡹ࠭य़"), bstack111lll1l1_opy_ (u"࠭ࡦࡶ࡮࡯ࡖࡪࡹࡥࡵࠩॠ"),
  bstack111lll1l1_opy_ (u"ࠧࡤ࡮ࡨࡥࡷ࡙ࡹࡴࡶࡨࡱࡋ࡯࡬ࡦࡵࠪॡ"),
  bstack111lll1l1_opy_ (u"ࠨࡧࡹࡩࡳࡺࡔࡪ࡯࡬ࡲ࡬ࡹࠧॢ"),
  bstack111lll1l1_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡒࡨࡶ࡫ࡵࡲ࡮ࡣࡱࡧࡪࡒ࡯ࡨࡩ࡬ࡲ࡬࠭ॣ"),
  bstack111lll1l1_opy_ (u"ࠪࡳࡹ࡮ࡥࡳࡃࡳࡴࡸ࠭।"),
  bstack111lll1l1_opy_ (u"ࠫࡵࡸࡩ࡯ࡶࡓࡥ࡬࡫ࡓࡰࡷࡵࡧࡪࡕ࡮ࡇ࡫ࡱࡨࡋࡧࡩ࡭ࡷࡵࡩࠬ॥"),
  bstack111lll1l1_opy_ (u"ࠬࡧࡰࡱࡃࡦࡸ࡮ࡼࡩࡵࡻࠪ०"), bstack111lll1l1_opy_ (u"࠭ࡡࡱࡲࡓࡥࡨࡱࡡࡨࡧࠪ१"), bstack111lll1l1_opy_ (u"ࠧࡢࡲࡳ࡛ࡦ࡯ࡴࡂࡥࡷ࡭ࡻ࡯ࡴࡺࠩ२"), bstack111lll1l1_opy_ (u"ࠨࡣࡳࡴ࡜ࡧࡩࡵࡒࡤࡧࡰࡧࡧࡦࠩ३"), bstack111lll1l1_opy_ (u"ࠩࡤࡴࡵ࡝ࡡࡪࡶࡇࡹࡷࡧࡴࡪࡱࡱࠫ४"),
  bstack111lll1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡕࡩࡦࡪࡹࡕ࡫ࡰࡩࡴࡻࡴࠨ५"),
  bstack111lll1l1_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡗࡩࡸࡺࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠨ६"),
  bstack111lll1l1_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡉ࡯ࡷࡧࡵࡥ࡬࡫ࠧ७"), bstack111lll1l1_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡃࡰࡸࡨࡶࡦ࡭ࡥࡆࡰࡧࡍࡳࡺࡥ࡯ࡶࠪ८"),
  bstack111lll1l1_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡅࡧࡹ࡭ࡨ࡫ࡒࡦࡣࡧࡽ࡙࡯࡭ࡦࡱࡸࡸࠬ९"),
  bstack111lll1l1_opy_ (u"ࠨࡣࡧࡦࡕࡵࡲࡵࠩ॰"),
  bstack111lll1l1_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡇࡩࡻ࡯ࡣࡦࡕࡲࡧࡰ࡫ࡴࠨॱ"),
  bstack111lll1l1_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡍࡳࡹࡴࡢ࡮࡯ࡘ࡮ࡳࡥࡰࡷࡷࠫॲ"),
  bstack111lll1l1_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡎࡴࡳࡵࡣ࡯ࡰࡕࡧࡴࡩࠩॳ"),
  bstack111lll1l1_opy_ (u"ࠬࡧࡶࡥࠩॴ"), bstack111lll1l1_opy_ (u"࠭ࡡࡷࡦࡏࡥࡺࡴࡣࡩࡖ࡬ࡱࡪࡵࡵࡵࠩॵ"), bstack111lll1l1_opy_ (u"ࠧࡢࡸࡧࡖࡪࡧࡤࡺࡖ࡬ࡱࡪࡵࡵࡵࠩॶ"), bstack111lll1l1_opy_ (u"ࠨࡣࡹࡨࡆࡸࡧࡴࠩॷ"),
  bstack111lll1l1_opy_ (u"ࠩࡸࡷࡪࡑࡥࡺࡵࡷࡳࡷ࡫ࠧॸ"), bstack111lll1l1_opy_ (u"ࠪ࡯ࡪࡿࡳࡵࡱࡵࡩࡕࡧࡴࡩࠩॹ"), bstack111lll1l1_opy_ (u"ࠫࡰ࡫ࡹࡴࡶࡲࡶࡪࡖࡡࡴࡵࡺࡳࡷࡪࠧॺ"),
  bstack111lll1l1_opy_ (u"ࠬࡱࡥࡺࡃ࡯࡭ࡦࡹࠧॻ"), bstack111lll1l1_opy_ (u"࠭࡫ࡦࡻࡓࡥࡸࡹࡷࡰࡴࡧࠫॼ"),
  bstack111lll1l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡋࡸࡦࡥࡸࡸࡦࡨ࡬ࡦࠩॽ"), bstack111lll1l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡁࡳࡩࡶࠫॾ"), bstack111lll1l1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡆࡺࡨࡧࡺࡺࡡࡣ࡮ࡨࡈ࡮ࡸࠧॿ"), bstack111lll1l1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡅ࡫ࡶࡴࡳࡥࡎࡣࡳࡴ࡮ࡴࡧࡇ࡫࡯ࡩࠬঀ"), bstack111lll1l1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡘࡷࡪ࡙ࡹࡴࡶࡨࡱࡊࡾࡥࡤࡷࡷࡥࡧࡲࡥࠨঁ"),
  bstack111lll1l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡔࡴࡸࡴࠨং"), bstack111lll1l1_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡕࡵࡲࡵࡵࠪঃ"),
  bstack111lll1l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡊࡩࡴࡣࡥࡰࡪࡈࡵࡪ࡮ࡧࡇ࡭࡫ࡣ࡬ࠩ঄"),
  bstack111lll1l1_opy_ (u"ࠨࡣࡸࡸࡴ࡝ࡥࡣࡸ࡬ࡩࡼ࡚ࡩ࡮ࡧࡲࡹࡹ࠭অ"),
  bstack111lll1l1_opy_ (u"ࠩ࡬ࡲࡹ࡫࡮ࡵࡃࡦࡸ࡮ࡵ࡮ࠨআ"), bstack111lll1l1_opy_ (u"ࠪ࡭ࡳࡺࡥ࡯ࡶࡆࡥࡹ࡫ࡧࡰࡴࡼࠫই"), bstack111lll1l1_opy_ (u"ࠫ࡮ࡴࡴࡦࡰࡷࡊࡱࡧࡧࡴࠩঈ"), bstack111lll1l1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡦࡲࡉ࡯ࡶࡨࡲࡹࡇࡲࡨࡷࡰࡩࡳࡺࡳࠨউ"),
  bstack111lll1l1_opy_ (u"࠭ࡤࡰࡰࡷࡗࡹࡵࡰࡂࡲࡳࡓࡳࡘࡥࡴࡧࡷࠫঊ"),
  bstack111lll1l1_opy_ (u"ࠧࡶࡰ࡬ࡧࡴࡪࡥࡌࡧࡼࡦࡴࡧࡲࡥࠩঋ"), bstack111lll1l1_opy_ (u"ࠨࡴࡨࡷࡪࡺࡋࡦࡻࡥࡳࡦࡸࡤࠨঌ"),
  bstack111lll1l1_opy_ (u"ࠩࡱࡳࡘ࡯ࡧ࡯ࠩ঍"),
  bstack111lll1l1_opy_ (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࡘࡲ࡮ࡳࡰࡰࡴࡷࡥࡳࡺࡖࡪࡧࡺࡷࠬ঎"),
  bstack111lll1l1_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡴࡤࡳࡱ࡬ࡨ࡜ࡧࡴࡤࡪࡨࡶࡸ࠭এ"),
  bstack111lll1l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬঐ"),
  bstack111lll1l1_opy_ (u"࠭ࡲࡦࡥࡵࡩࡦࡺࡥࡄࡪࡵࡳࡲ࡫ࡄࡳ࡫ࡹࡩࡷ࡙ࡥࡴࡵ࡬ࡳࡳࡹࠧ঑"),
  bstack111lll1l1_opy_ (u"ࠧ࡯ࡣࡷ࡭ࡻ࡫ࡗࡦࡤࡖࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࠭঒"),
  bstack111lll1l1_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡕࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡕࡧࡴࡩࠩও"),
  bstack111lll1l1_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡖࡴࡪ࡫ࡤࠨঔ"),
  bstack111lll1l1_opy_ (u"ࠪ࡫ࡵࡹࡅ࡯ࡣࡥࡰࡪࡪࠧক"),
  bstack111lll1l1_opy_ (u"ࠫ࡮ࡹࡈࡦࡣࡧࡰࡪࡹࡳࠨখ"),
  bstack111lll1l1_opy_ (u"ࠬࡧࡤࡣࡇࡻࡩࡨ࡚ࡩ࡮ࡧࡲࡹࡹ࠭গ"),
  bstack111lll1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡪ࡙ࡣࡳ࡫ࡳࡸࠬঘ"),
  bstack111lll1l1_opy_ (u"ࠧࡴ࡭࡬ࡴࡉ࡫ࡶࡪࡥࡨࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠫঙ"),
  bstack111lll1l1_opy_ (u"ࠨࡣࡸࡸࡴࡍࡲࡢࡰࡷࡔࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳࠨচ"),
  bstack111lll1l1_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡑࡥࡹࡻࡲࡢ࡮ࡒࡶ࡮࡫࡮ࡵࡣࡷ࡭ࡴࡴࠧছ"),
  bstack111lll1l1_opy_ (u"ࠪࡷࡾࡹࡴࡦ࡯ࡓࡳࡷࡺࠧজ"),
  bstack111lll1l1_opy_ (u"ࠫࡷ࡫࡭ࡰࡶࡨࡅࡩࡨࡈࡰࡵࡷࠫঝ"),
  bstack111lll1l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡘࡲࡱࡵࡣ࡬ࠩঞ"), bstack111lll1l1_opy_ (u"࠭ࡵ࡯࡮ࡲࡧࡰ࡚ࡹࡱࡧࠪট"), bstack111lll1l1_opy_ (u"ࠧࡶࡰ࡯ࡳࡨࡱࡋࡦࡻࠪঠ"),
  bstack111lll1l1_opy_ (u"ࠨࡣࡸࡸࡴࡒࡡࡶࡰࡦ࡬ࠬড"),
  bstack111lll1l1_opy_ (u"ࠩࡶ࡯࡮ࡶࡌࡰࡩࡦࡥࡹࡉࡡࡱࡶࡸࡶࡪ࠭ঢ"),
  bstack111lll1l1_opy_ (u"ࠪࡹࡳ࡯࡮ࡴࡶࡤࡰࡱࡕࡴࡩࡧࡵࡔࡦࡩ࡫ࡢࡩࡨࡷࠬণ"),
  bstack111lll1l1_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩ࡜࡯࡮ࡥࡱࡺࡅࡳ࡯࡭ࡢࡶ࡬ࡳࡳ࠭ত"),
  bstack111lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡘࡴࡵ࡬ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩথ"),
  bstack111lll1l1_opy_ (u"࠭ࡥ࡯ࡨࡲࡶࡨ࡫ࡁࡱࡲࡌࡲࡸࡺࡡ࡭࡮ࠪদ"),
  bstack111lll1l1_opy_ (u"ࠧࡦࡰࡶࡹࡷ࡫ࡗࡦࡤࡹ࡭ࡪࡽࡳࡉࡣࡹࡩࡕࡧࡧࡦࡵࠪধ"), bstack111lll1l1_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࡆࡨࡺࡹࡵ࡯࡭ࡵࡓࡳࡷࡺࠧন"), bstack111lll1l1_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦ࡙ࡨࡦࡻ࡯ࡥࡸࡆࡨࡸࡦ࡯࡬ࡴࡅࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠬ঩"),
  bstack111lll1l1_opy_ (u"ࠪࡶࡪࡳ࡯ࡵࡧࡄࡴࡵࡹࡃࡢࡥ࡫ࡩࡑ࡯࡭ࡪࡶࠪপ"),
  bstack111lll1l1_opy_ (u"ࠫࡨࡧ࡬ࡦࡰࡧࡥࡷࡌ࡯ࡳ࡯ࡤࡸࠬফ"),
  bstack111lll1l1_opy_ (u"ࠬࡨࡵ࡯ࡦ࡯ࡩࡎࡪࠧব"),
  bstack111lll1l1_opy_ (u"࠭࡬ࡢࡷࡱࡧ࡭࡚ࡩ࡮ࡧࡲࡹࡹ࠭ভ"),
  bstack111lll1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࡕࡨࡶࡻ࡯ࡣࡦࡵࡈࡲࡦࡨ࡬ࡦࡦࠪম"), bstack111lll1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࡖࡩࡷࡼࡩࡤࡧࡶࡅࡺࡺࡨࡰࡴ࡬ࡾࡪࡪࠧয"),
  bstack111lll1l1_opy_ (u"ࠩࡤࡹࡹࡵࡁࡤࡥࡨࡴࡹࡇ࡬ࡦࡴࡷࡷࠬর"), bstack111lll1l1_opy_ (u"ࠪࡥࡺࡺ࡯ࡅ࡫ࡶࡱ࡮ࡹࡳࡂ࡮ࡨࡶࡹࡹࠧ঱"),
  bstack111lll1l1_opy_ (u"ࠫࡳࡧࡴࡪࡸࡨࡍࡳࡹࡴࡳࡷࡰࡩࡳࡺࡳࡍ࡫ࡥࠫল"),
  bstack111lll1l1_opy_ (u"ࠬࡴࡡࡵ࡫ࡹࡩ࡜࡫ࡢࡕࡣࡳࠫ঳"),
  bstack111lll1l1_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡏ࡮ࡪࡶ࡬ࡥࡱ࡛ࡲ࡭ࠩ঴"), bstack111lll1l1_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡁ࡭࡮ࡲࡻࡕࡵࡰࡶࡲࡶࠫ঵"), bstack111lll1l1_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࡊࡩࡱࡳࡷ࡫ࡆࡳࡣࡸࡨ࡜ࡧࡲ࡯࡫ࡱ࡫ࠬশ"), bstack111lll1l1_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࡑࡳࡩࡳࡒࡩ࡯࡭ࡶࡍࡳࡈࡡࡤ࡭ࡪࡶࡴࡻ࡮ࡥࠩষ"),
  bstack111lll1l1_opy_ (u"ࠪ࡯ࡪ࡫ࡰࡌࡧࡼࡇ࡭ࡧࡩ࡯ࡵࠪস"),
  bstack111lll1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮࡬ࡾࡦࡨ࡬ࡦࡕࡷࡶ࡮ࡴࡧࡴࡆ࡬ࡶࠬহ"),
  bstack111lll1l1_opy_ (u"ࠬࡶࡲࡰࡥࡨࡷࡸࡇࡲࡨࡷࡰࡩࡳࡺࡳࠨ঺"),
  bstack111lll1l1_opy_ (u"࠭ࡩ࡯ࡶࡨࡶࡐ࡫ࡹࡅࡧ࡯ࡥࡾ࠭঻"),
  bstack111lll1l1_opy_ (u"ࠧࡴࡪࡲࡻࡎࡕࡓࡍࡱࡪ়ࠫ"),
  bstack111lll1l1_opy_ (u"ࠨࡵࡨࡲࡩࡑࡥࡺࡕࡷࡶࡦࡺࡥࡨࡻࠪঽ"),
  bstack111lll1l1_opy_ (u"ࠩࡺࡩࡧࡱࡩࡵࡔࡨࡷࡵࡵ࡮ࡴࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪা"), bstack111lll1l1_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡗࡢ࡫ࡷࡘ࡮ࡳࡥࡰࡷࡷࠫি"),
  bstack111lll1l1_opy_ (u"ࠫࡷ࡫࡭ࡰࡶࡨࡈࡪࡨࡵࡨࡒࡵࡳࡽࡿࠧী"),
  bstack111lll1l1_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡆࡹࡹ࡯ࡥࡈࡼࡪࡩࡵࡵࡧࡉࡶࡴࡳࡈࡵࡶࡳࡷࠬু"),
  bstack111lll1l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡐࡴ࡭ࡃࡢࡲࡷࡹࡷ࡫ࠧূ"),
  bstack111lll1l1_opy_ (u"ࠧࡸࡧࡥ࡯࡮ࡺࡄࡦࡤࡸ࡫ࡕࡸ࡯ࡹࡻࡓࡳࡷࡺࠧৃ"),
  bstack111lll1l1_opy_ (u"ࠨࡨࡸࡰࡱࡉ࡯࡯ࡶࡨࡼࡹࡒࡩࡴࡶࠪৄ"),
  bstack111lll1l1_opy_ (u"ࠩࡺࡥ࡮ࡺࡆࡰࡴࡄࡴࡵ࡙ࡣࡳ࡫ࡳࡸࠬ৅"),
  bstack111lll1l1_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࡇࡴࡴ࡮ࡦࡥࡷࡖࡪࡺࡲࡪࡧࡶࠫ৆"),
  bstack111lll1l1_opy_ (u"ࠫࡦࡶࡰࡏࡣࡰࡩࠬে"),
  bstack111lll1l1_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡘ࡙ࡌࡄࡧࡵࡸࠬৈ"),
  bstack111lll1l1_opy_ (u"࠭ࡴࡢࡲ࡚࡭ࡹ࡮ࡓࡩࡱࡵࡸࡕࡸࡥࡴࡵࡇࡹࡷࡧࡴࡪࡱࡱࠫ৉"),
  bstack111lll1l1_opy_ (u"ࠧࡴࡥࡤࡰࡪࡌࡡࡤࡶࡲࡶࠬ৊"),
  bstack111lll1l1_opy_ (u"ࠨࡹࡧࡥࡑࡵࡣࡢ࡮ࡓࡳࡷࡺࠧো"),
  bstack111lll1l1_opy_ (u"ࠩࡶ࡬ࡴࡽࡘࡤࡱࡧࡩࡑࡵࡧࠨৌ"),
  bstack111lll1l1_opy_ (u"ࠪ࡭ࡴࡹࡉ࡯ࡵࡷࡥࡱࡲࡐࡢࡷࡶࡩ্ࠬ"),
  bstack111lll1l1_opy_ (u"ࠫࡽࡩ࡯ࡥࡧࡆࡳࡳ࡬ࡩࡨࡈ࡬ࡰࡪ࠭ৎ"),
  bstack111lll1l1_opy_ (u"ࠬࡱࡥࡺࡥ࡫ࡥ࡮ࡴࡐࡢࡵࡶࡻࡴࡸࡤࠨ৏"),
  bstack111lll1l1_opy_ (u"࠭ࡵࡴࡧࡓࡶࡪࡨࡵࡪ࡮ࡷ࡛ࡉࡇࠧ৐"),
  bstack111lll1l1_opy_ (u"ࠧࡱࡴࡨࡺࡪࡴࡴࡘࡆࡄࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠨ৑"),
  bstack111lll1l1_opy_ (u"ࠨࡹࡨࡦࡉࡸࡩࡷࡧࡵࡅ࡬࡫࡮ࡵࡗࡵࡰࠬ৒"),
  bstack111lll1l1_opy_ (u"ࠩ࡮ࡩࡾࡩࡨࡢ࡫ࡱࡔࡦࡺࡨࠨ৓"),
  bstack111lll1l1_opy_ (u"ࠪࡹࡸ࡫ࡎࡦࡹ࡚ࡈࡆ࠭৔"),
  bstack111lll1l1_opy_ (u"ࠫࡼࡪࡡࡍࡣࡸࡲࡨ࡮ࡔࡪ࡯ࡨࡳࡺࡺࠧ৕"), bstack111lll1l1_opy_ (u"ࠬࡽࡤࡢࡅࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲ࡙࡯࡭ࡦࡱࡸࡸࠬ৖"),
  bstack111lll1l1_opy_ (u"࠭ࡸࡤࡱࡧࡩࡔࡸࡧࡊࡦࠪৗ"), bstack111lll1l1_opy_ (u"ࠧࡹࡥࡲࡨࡪ࡙ࡩࡨࡰ࡬ࡲ࡬ࡏࡤࠨ৘"),
  bstack111lll1l1_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡥ࡙ࡇࡅࡇࡻ࡮ࡥ࡮ࡨࡍࡩ࠭৙"),
  bstack111lll1l1_opy_ (u"ࠩࡵࡩࡸ࡫ࡴࡐࡰࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡸࡴࡐࡰ࡯ࡽࠬ৚"),
  bstack111lll1l1_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡘ࡮ࡳࡥࡰࡷࡷࡷࠬ৛"),
  bstack111lll1l1_opy_ (u"ࠫࡼࡪࡡࡔࡶࡤࡶࡹࡻࡰࡓࡧࡷࡶ࡮࡫ࡳࠨড়"), bstack111lll1l1_opy_ (u"ࠬࡽࡤࡢࡕࡷࡥࡷࡺࡵࡱࡔࡨࡸࡷࡿࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠨঢ়"),
  bstack111lll1l1_opy_ (u"࠭ࡣࡰࡰࡱࡩࡨࡺࡈࡢࡴࡧࡻࡦࡸࡥࡌࡧࡼࡦࡴࡧࡲࡥࠩ৞"),
  bstack111lll1l1_opy_ (u"ࠧ࡮ࡣࡻࡘࡾࡶࡩ࡯ࡩࡉࡶࡪࡷࡵࡦࡰࡦࡽࠬয়"),
  bstack111lll1l1_opy_ (u"ࠨࡵ࡬ࡱࡵࡲࡥࡊࡵ࡙࡭ࡸ࡯ࡢ࡭ࡧࡆ࡬ࡪࡩ࡫ࠨৠ"),
  bstack111lll1l1_opy_ (u"ࠩࡸࡷࡪࡉࡡࡳࡶ࡫ࡥ࡬࡫ࡓࡴ࡮ࠪৡ"),
  bstack111lll1l1_opy_ (u"ࠪࡷ࡭ࡵࡵ࡭ࡦࡘࡷࡪ࡙ࡩ࡯ࡩ࡯ࡩࡹࡵ࡮ࡕࡧࡶࡸࡒࡧ࡮ࡢࡩࡨࡶࠬৢ"),
  bstack111lll1l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡌ࡛ࡉࡖࠧৣ"),
  bstack111lll1l1_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡘࡴࡻࡣࡩࡋࡧࡉࡳࡸ࡯࡭࡮ࠪ৤"),
  bstack111lll1l1_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪࡎࡩࡥࡦࡨࡲࡆࡶࡩࡑࡱ࡯࡭ࡨࡿࡅࡳࡴࡲࡶࠬ৥"),
  bstack111lll1l1_opy_ (u"ࠧ࡮ࡱࡦ࡯ࡑࡵࡣࡢࡶ࡬ࡳࡳࡇࡰࡱࠩ০"),
  bstack111lll1l1_opy_ (u"ࠨ࡮ࡲ࡫ࡨࡧࡴࡇࡱࡵࡱࡦࡺࠧ১"), bstack111lll1l1_opy_ (u"ࠩ࡯ࡳ࡬ࡩࡡࡵࡈ࡬ࡰࡹ࡫ࡲࡔࡲࡨࡧࡸ࠭২"),
  bstack111lll1l1_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡆࡨࡰࡦࡿࡁࡥࡤࠪ৩")
]
bstack1ll1ll1ll_opy_ = bstack111lll1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠯ࡦࡰࡴࡻࡤ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡹࡵࡲ࡯ࡢࡦࠪ৪")
bstack1l1ll11l1_opy_ = [bstack111lll1l1_opy_ (u"ࠬ࠴ࡡࡱ࡭ࠪ৫"), bstack111lll1l1_opy_ (u"࠭࠮ࡢࡣࡥࠫ৬"), bstack111lll1l1_opy_ (u"ࠧ࠯࡫ࡳࡥࠬ৭")]
bstack1llll11ll_opy_ = [bstack111lll1l1_opy_ (u"ࠨ࡫ࡧࠫ৮"), bstack111lll1l1_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ৯"), bstack111lll1l1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭ৰ"), bstack111lll1l1_opy_ (u"ࠫࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦࠪৱ")]
bstack1ll1l11ll_opy_ = {
  bstack111lll1l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ৲"): bstack111lll1l1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ৳"),
  bstack111lll1l1_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨ৴"): bstack111lll1l1_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭৵"),
  bstack111lll1l1_opy_ (u"ࠩࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ৶"): bstack111lll1l1_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫ৷"),
  bstack111lll1l1_opy_ (u"ࠫ࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ৸"): bstack111lll1l1_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫ৹"),
  bstack111lll1l1_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡕࡰࡵ࡫ࡲࡲࡸ࠭৺"): bstack111lll1l1_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ৻")
}
bstack1ll1l1lll_opy_ = [
  bstack111lll1l1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ৼ"),
  bstack111lll1l1_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧ৽"),
  bstack111lll1l1_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫ৾"),
  bstack111lll1l1_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ৿"),
  bstack111lll1l1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭਀"),
]
bstack11l11l11_opy_ = bstack1l111l1l1_opy_ + bstack1lll1lll1_opy_ + bstack11111l11_opy_
bstack1llll11l1_opy_ = [
  bstack111lll1l1_opy_ (u"࠭࡞࡭ࡱࡦࡥࡱ࡮࡯ࡴࡶࠧࠫਁ"),
  bstack111lll1l1_opy_ (u"ࠧ࡟ࡤࡶ࠱ࡱࡵࡣࡢ࡮࠱ࡧࡴࡳࠤࠨਂ"),
  bstack111lll1l1_opy_ (u"ࠨࡠ࠴࠶࠼࠴ࠧਃ"),
  bstack111lll1l1_opy_ (u"ࠩࡡ࠵࠵࠴ࠧ਄"),
  bstack111lll1l1_opy_ (u"ࠪࡢ࠶࠽࠲࠯࠳࡞࠺࠲࠿࡝࠯ࠩਅ"),
  bstack111lll1l1_opy_ (u"ࠫࡣ࠷࠷࠳࠰࠵࡟࠵࠳࠹࡞࠰ࠪਆ"),
  bstack111lll1l1_opy_ (u"ࠬࡤ࠱࠸࠴࠱࠷ࡠ࠶࠭࠲࡟࠱ࠫਇ"),
  bstack111lll1l1_opy_ (u"࠭࡞࠲࠻࠵࠲࠶࠼࠸࠯ࠩਈ")
]
bstack11l1lll1_opy_ = bstack111lll1l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡽࢀࠫਉ")
bstack11l1ll1_opy_ = bstack111lll1l1_opy_ (u"ࠨࡵࡧ࡯࠴ࡼ࠱࠰ࡧࡹࡩࡳࡺࠧਊ")
bstack1l1l_opy_ = [ bstack111lll1l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ਋") ]
bstack1ll11ll11_opy_ = [ bstack111lll1l1_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩ਌") ]
bstack11ll1ll1_opy_ = [ bstack111lll1l1_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ਍") ]
bstack1ll1l1111_opy_ = bstack111lll1l1_opy_ (u"࡙ࠬࡄࡌࡕࡨࡸࡺࡶࠧ਎")
bstack11lll1_opy_ = bstack111lll1l1_opy_ (u"࠭ࡓࡅࡍࡗࡩࡸࡺࡁࡵࡶࡨࡱࡵࡺࡥࡥࠩਏ")
bstack111l1l11_opy_ = bstack111lll1l1_opy_ (u"ࠧࡔࡆࡎࡘࡪࡹࡴࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠫਐ")
bstack11l1l1ll1_opy_ = bstack111lll1l1_opy_ (u"ࠨ࠶࠱࠴࠳࠶ࠧ਑")
bstack111l1l_opy_ = [
  bstack111lll1l1_opy_ (u"ࠩࡈࡖࡗࡥࡆࡂࡋࡏࡉࡉ࠭਒"),
  bstack111lll1l1_opy_ (u"ࠪࡉࡗࡘ࡟ࡕࡋࡐࡉࡉࡥࡏࡖࡖࠪਓ"),
  bstack111lll1l1_opy_ (u"ࠫࡊࡘࡒࡠࡄࡏࡓࡈࡑࡅࡅࡡࡅ࡝ࡤࡉࡌࡊࡇࡑࡘࠬਔ"),
  bstack111lll1l1_opy_ (u"ࠬࡋࡒࡓࡡࡑࡉ࡙࡝ࡏࡓࡍࡢࡇࡍࡇࡎࡈࡇࡇࠫਕ"),
  bstack111lll1l1_opy_ (u"࠭ࡅࡓࡔࡢࡗࡔࡉࡋࡆࡖࡢࡒࡔ࡚࡟ࡄࡑࡑࡒࡊࡉࡔࡆࡆࠪਖ"),
  bstack111lll1l1_opy_ (u"ࠧࡆࡔࡕࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡅࡏࡓࡘࡋࡄࠨਗ"),
  bstack111lll1l1_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡕࡉࡘࡋࡔࠨਘ"),
  bstack111lll1l1_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡖࡊࡌࡕࡔࡇࡇࠫਙ"),
  bstack111lll1l1_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡆࡈࡏࡓࡖࡈࡈࠬਚ"),
  bstack111lll1l1_opy_ (u"ࠫࡊࡘࡒࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬਛ"),
  bstack111lll1l1_opy_ (u"ࠬࡋࡒࡓࡡࡑࡅࡒࡋ࡟ࡏࡑࡗࡣࡗࡋࡓࡐࡎ࡙ࡉࡉ࠭ਜ"),
  bstack111lll1l1_opy_ (u"࠭ࡅࡓࡔࡢࡅࡉࡊࡒࡆࡕࡖࡣࡎࡔࡖࡂࡎࡌࡈࠬਝ"),
  bstack111lll1l1_opy_ (u"ࠧࡆࡔࡕࡣࡆࡊࡄࡓࡇࡖࡗࡤ࡛ࡎࡓࡇࡄࡇࡍࡇࡂࡍࡇࠪਞ"),
  bstack111lll1l1_opy_ (u"ࠨࡇࡕࡖࡤ࡚ࡕࡏࡐࡈࡐࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡉࡅࡎࡒࡅࡅࠩਟ"),
  bstack111lll1l1_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡘࡎࡓࡅࡅࡡࡒ࡙࡙࠭ਠ"),
  bstack111lll1l1_opy_ (u"ࠪࡉࡗࡘ࡟ࡔࡑࡆࡏࡘࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪਡ"),
  bstack111lll1l1_opy_ (u"ࠫࡊࡘࡒࡠࡕࡒࡇࡐ࡙࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡍࡕࡓࡕࡡࡘࡒࡗࡋࡁࡄࡊࡄࡆࡑࡋࠧਢ"),
  bstack111lll1l1_opy_ (u"ࠬࡋࡒࡓࡡࡓࡖࡔ࡞࡙ࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬਣ"),
  bstack111lll1l1_opy_ (u"࠭ࡅࡓࡔࡢࡒࡆࡓࡅࡠࡐࡒࡘࡤࡘࡅࡔࡑࡏ࡚ࡊࡊࠧਤ"),
  bstack111lll1l1_opy_ (u"ࠧࡆࡔࡕࡣࡓࡇࡍࡆࡡࡕࡉࡘࡕࡌࡖࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭ਥ"),
  bstack111lll1l1_opy_ (u"ࠨࡇࡕࡖࡤࡓࡁࡏࡆࡄࡘࡔࡘ࡙ࡠࡒࡕࡓ࡝࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧਦ"),
]
bstack11ll1ll11_opy_ = bstack111lll1l1_opy_ (u"ࠩ࠱࠳ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡥࡷࡺࡩࡧࡣࡦࡸࡸ࠵ࠧਧ")
def bstack111l1ll_opy_():
  global CONFIG
  headers = {
        bstack111lll1l1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩਨ"): bstack111lll1l1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ਩"),
      }
  proxies = bstack1ll11ll1_opy_(CONFIG, bstack1ll1lll11_opy_)
  try:
    response = requests.get(bstack1ll1lll11_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l11l1lll_opy_ = response.json()[bstack111lll1l1_opy_ (u"ࠬ࡮ࡵࡣࡵࠪਪ")]
      logger.debug(bstack1l1l1l1_opy_.format(response.json()))
      return bstack1l11l1lll_opy_
    else:
      logger.debug(bstack1l11l1ll1_opy_.format(bstack111lll1l1_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧਫ")))
  except Exception as e:
    logger.debug(bstack1l11l1ll1_opy_.format(e))
def bstack11ll1lll1_opy_(hub_url):
  global CONFIG
  url = bstack111lll1l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤਬ")+  hub_url + bstack111lll1l1_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣਭ")
  headers = {
        bstack111lll1l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨਮ"): bstack111lll1l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ਯ"),
      }
  proxies = bstack1ll11ll1_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11ll11_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1l11lll1l_opy_.format(hub_url, e))
def bstack1lll11ll1_opy_():
  try:
    global bstack111llll1_opy_
    bstack1l11l1lll_opy_ = bstack111l1ll_opy_()
    bstack11llll1l1_opy_ = []
    results = []
    for bstack111lll1l_opy_ in bstack1l11l1lll_opy_:
      bstack11llll1l1_opy_.append(bstack1l111111l_opy_(target=bstack11ll1lll1_opy_,args=(bstack111lll1l_opy_,)))
    for t in bstack11llll1l1_opy_:
      t.start()
    for t in bstack11llll1l1_opy_:
      results.append(t.join())
    bstack11lllll1l_opy_ = {}
    for item in results:
      hub_url = item[bstack111lll1l1_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬਰ")]
      latency = item[bstack111lll1l1_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭਱")]
      bstack11lllll1l_opy_[hub_url] = latency
    bstack11ll1l_opy_ = min(bstack11lllll1l_opy_, key= lambda x: bstack11lllll1l_opy_[x])
    bstack111llll1_opy_ = bstack11ll1l_opy_
    logger.debug(bstack1llllll_opy_.format(bstack11ll1l_opy_))
  except Exception as e:
    logger.debug(bstack1ll1_opy_.format(e))
bstack1l1ll1111_opy_ = bstack111lll1l1_opy_ (u"࠭ࡓࡦࡶࡷ࡭ࡳ࡭ࠠࡶࡲࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠼ࠣࡿࢂ࠭ਲ")
bstack1l1l11111_opy_ = bstack111lll1l1_opy_ (u"ࠧࡄࡱࡰࡴࡱ࡫ࡴࡦࡦࠣࡷࡪࡺࡵࡱࠣࠪਲ਼")
bstack11l11l1ll_opy_ = bstack111lll1l1_opy_ (u"ࠨࡒࡤࡶࡸ࡫ࡤࠡࡥࡲࡲ࡫࡯ࡧࠡࡨ࡬ࡰࡪࡀࠠࡼࡿࠪ਴")
bstack1111l_opy_ = bstack111lll1l1_opy_ (u"ࠩࡖࡥࡳ࡯ࡴࡪࡼࡨࡨࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࢀࢃࠧਵ")
bstack11ll11ll1_opy_ = bstack111lll1l1_opy_ (u"࡙ࠪࡸ࡯࡮ࡨࠢ࡫ࡹࡧࠦࡵࡳ࡮࠽ࠤࢀࢃࠧਸ਼")
bstack1ll1l1_opy_ = bstack111lll1l1_opy_ (u"ࠫࡘ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡴࡷࡩࡩࠦࡷࡪࡶ࡫ࠤ࡮ࡪ࠺ࠡࡽࢀࠫ਷")
bstack11l1l1l1l_opy_ = bstack111lll1l1_opy_ (u"ࠬࡘࡥࡤࡧ࡬ࡺࡪࡪࠠࡪࡰࡷࡩࡷࡸࡵࡱࡶ࠯ࠤࡪࡾࡩࡵ࡫ࡱ࡫ࠬਸ")
bstack1ll111l1_opy_ = bstack111lll1l1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠢࡷࡳࠥࡸࡵ࡯ࠢࡷࡩࡸࡺࡳ࠯ࠢࡣࡴ࡮ࡶࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡵࡨࡰࡪࡴࡩࡶ࡯ࡣࠫਹ")
bstack1l11l1l1l_opy_ = bstack111lll1l1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴࠡࡣࡱࡨࠥࡶࡹࡵࡧࡶࡸ࠲ࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠠࡱࡣࡦ࡯ࡦ࡭ࡥࡴ࠰ࠣࡤࡵ࡯ࡰࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡶࡩࡱ࡫࡮ࡪࡷࡰࡤࠬ਺")
bstack111ll1lll_opy_ = bstack111lll1l1_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡄࡴࡵ࡯ࡵ࡮ࡎ࡬ࡦࡷࡧࡲࡺࠢࡳࡥࡨࡱࡡࡨࡧ࠱ࠤࡥࡶࡩࡱࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡶࡴࡨ࡯ࡵࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࠱ࡦࡶࡰࡪࡷࡰࡰ࡮ࡨࡲࡢࡴࡼࡤࠬ਻")
bstack1l1llllll_opy_ = bstack111lll1l1_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡶࡴࡨ࡯ࡵ࠮ࠣࡴࡦࡨ࡯ࡵࠢࡤࡲࡩࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࡭࡫ࡥࡶࡦࡸࡹࠡࡲࡤࡧࡰࡧࡧࡦࡵࠣࡸࡴࠦࡲࡶࡰࠣࡶࡴࡨ࡯ࡵࠢࡷࡩࡸࡺࡳࠡ࡫ࡱࠤࡵࡧࡲࡢ࡮࡯ࡩࡱ࠴ࠠࡡࡲ࡬ࡴࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡲࡰࡤࡲࡸ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠࡳࡱࡥࡳࡹ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠮ࡲࡤࡦࡴࡺࠠࡳࡱࡥࡳࡹ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠮ࡵࡨࡰࡪࡴࡩࡶ࡯࡯࡭ࡧࡸࡡࡳࡻࡣ਼ࠫ")
bstack11l1l11_opy_ = bstack111lll1l1_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡧ࡫ࡨࡢࡸࡨࠤࡹࡵࠠࡳࡷࡱࠤࡹ࡫ࡳࡵࡵ࠱ࠤࡥࡶࡩࡱࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡦࡪ࡮ࡡࡷࡧࡣࠫ਽")
bstack1ll_opy_ = bstack111lll1l1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡧࡰࡱ࡫ࡸࡱ࠲ࡩ࡬ࡪࡧࡱࡸࠥࡺ࡯ࠡࡴࡸࡲࠥࡺࡥࡴࡶࡶ࠲ࠥࡦࡰࡪࡲࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡆࡶࡰࡪࡷࡰ࠱ࡕࡿࡴࡩࡱࡱ࠱ࡈࡲࡩࡦࡰࡷࡤࠬਾ")
bstack11l1ll1l_opy_ = bstack111lll1l1_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡸࡴࠦࡲࡶࡰࠣࡸࡪࡹࡴࡴ࠰ࠣࡤࡵ࡯ࡰࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡦࠧਿ")
bstack1ll1l111_opy_ = bstack111lll1l1_opy_ (u"࠭ࡃࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡩ࡭ࡳࡪࠠࡦ࡫ࡷ࡬ࡪࡸࠠࡔࡧ࡯ࡩࡳ࡯ࡵ࡮ࠢࡲࡶࠥࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡷࡳࠥࡸࡵ࡯ࠢࡷࡩࡸࡺࡳ࠯ࠢࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡹࡧ࡬࡭ࠢࡷ࡬ࡪࠦࡲࡦ࡮ࡨࡺࡦࡴࡴࠡࡲࡤࡧࡰࡧࡧࡦࡵࠣࡹࡸ࡯࡮ࡨࠢࡳ࡭ࡵࠦࡴࡰࠢࡵࡹࡳࠦࡴࡦࡵࡷࡷ࠳࠭ੀ")
bstack1ll1ll11_opy_ = bstack111lll1l1_opy_ (u"ࠧࡉࡣࡱࡨࡱ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡱࡵࡳࡦࠩੁ")
bstack111ll111_opy_ = bstack111lll1l1_opy_ (u"ࠨࡃ࡯ࡰࠥࡪ࡯࡯ࡧࠤࠫੂ")
bstack111ll1l1_opy_ = bstack111lll1l1_opy_ (u"ࠩࡆࡳࡳ࡬ࡩࡨࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴࠡࡣࡷࠤࡦࡴࡹࠡࡲࡤࡶࡪࡴࡴࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡴ࡬ࠠࠣࡽࢀࠦ࠳ࠦࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡥ࡯ࡹࡩ࡫ࠠࡢࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰ࠴ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡧ࡭࡭ࠢࡩ࡭ࡱ࡫ࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤ࡫ࡵࡲࠡࡶࡨࡷࡹࡹ࠮ࠨ੃")
bstack1lll1l1_opy_ = bstack111lll1l1_opy_ (u"ࠪࡆࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡦࡶࡪࡪࡥ࡯ࡶ࡬ࡥࡱࡹࠠ࡯ࡱࡷࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡢࡦࡧࠤࡹ࡮ࡥ࡮ࠢ࡬ࡲࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠡࡥࡲࡲ࡫࡯ࡧࠡࡨ࡬ࡰࡪࠦࡡࡴࠢࠥࡹࡸ࡫ࡲࡏࡣࡰࡩࠧࠦࡡ࡯ࡦࠣࠦࡦࡩࡣࡦࡵࡶࡏࡪࡿࠢࠡࡱࡵࠤࡸ࡫ࡴࠡࡶ࡫ࡩࡲࠦࡡࡴࠢࡨࡲࡻ࡯ࡲࡰࡰࡰࡩࡳࡺࠠࡷࡣࡵ࡭ࡦࡨ࡬ࡦࡵ࠽ࠤࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊࠨࠠࡢࡰࡧࠤࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠣࠩ੄")
bstack11l1l11l1_opy_ = bstack111lll1l1_opy_ (u"ࠫࡒࡧ࡬ࡧࡱࡵࡱࡪࡪࠠࡤࡱࡱࡪ࡮࡭ࠠࡧ࡫࡯ࡩ࠿ࠨࡻࡾࠤࠪ੅")
bstack1ll1ll1_opy_ = bstack111lll1l1_opy_ (u"ࠬࡋ࡮ࡤࡱࡸࡲࡹ࡫ࡲࡦࡦࠣࡩࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡸࡴࠥ࠳ࠠࡼࡿࠪ੆")
bstack1ll111ll1_opy_ = bstack111lll1l1_opy_ (u"࠭ࡓࡵࡣࡵࡸ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡍࡱࡦࡥࡱ࠭ੇ")
bstack11l11l1l1_opy_ = bstack111lll1l1_opy_ (u"ࠧࡔࡶࡲࡴࡵ࡯࡮ࡨࠢࡅࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡎࡲࡧࡦࡲࠧੈ")
bstack11l1l1lll_opy_ = bstack111lll1l1_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡍࡱࡦࡥࡱࠦࡩࡴࠢࡱࡳࡼࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠡࠨ੉")
bstack1l111l1ll_opy_ = bstack111lll1l1_opy_ (u"ࠩࡆࡳࡺࡲࡤࠡࡰࡲࡸࠥࡹࡴࡢࡴࡷࠤࡇࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡐࡴࡩࡡ࡭࠼ࠣࡿࢂ࠭੊")
bstack111llllll_opy_ = bstack111lll1l1_opy_ (u"ࠪࡗࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡲ࡯ࡤࡣ࡯ࠤࡧ࡯࡮ࡢࡴࡼࠤࡼ࡯ࡴࡩࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࢀࢃࠧੋ")
bstack1lll111_opy_ = bstack111lll1l1_opy_ (u"࡚ࠫࡶࡤࡢࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡥࡧࡷࡥ࡮ࡲࡳ࠻ࠢࡾࢁࠬੌ")
bstack11ll111ll_opy_ = bstack111lll1l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡷࡳࡨࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳࠡࡽࢀ੍ࠫ")
bstack1llll1l1_opy_ = bstack111lll1l1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡰࡳࡱࡹ࡭ࡩ࡫ࠠࡢࡰࠣࡥࡵࡶࡲࡰࡲࡵ࡭ࡦࡺࡥࠡࡈ࡚ࠤ࠭ࡸ࡯ࡣࡱࡷ࠳ࡵࡧࡢࡰࡶࠬࠤ࡮ࡴࠠࡤࡱࡱࡪ࡮࡭ࠠࡧ࡫࡯ࡩ࠱ࠦࡳ࡬࡫ࡳࠤࡹ࡮ࡥࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤࡰ࡫ࡹࠡ࡫ࡱࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࡮࡬ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡵ࡬ࡱࡵࡲࡥࠡࡲࡼࡸ࡭ࡵ࡮ࠡࡵࡦࡶ࡮ࡶࡴࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢࡤࡲࡾࠦࡆࡘ࠰ࠪ੎")
bstack1l1ll1ll1_opy_ = bstack111lll1l1_opy_ (u"ࠧࡔࡧࡷࡸ࡮ࡴࡧࠡࡪࡷࡸࡵࡖࡲࡰࡺࡼ࠳࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠡ࡫ࡶࠤࡳࡵࡴࠡࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤࡴࡴࠠࡤࡷࡵࡶࡪࡴࡴ࡭ࡻࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡰࡨࠣࡷࡪࡲࡥ࡯࡫ࡸࡱࠥ࠮ࡻࡾࠫ࠯ࠤࡵࡲࡥࡢࡵࡨࠤࡺࡶࡧࡳࡣࡧࡩࠥࡺ࡯ࠡࡕࡨࡰࡪࡴࡩࡶ࡯ࡁࡁ࠹࠴࠰࠯࠲ࠣࡳࡷࠦࡲࡦࡨࡨࡶࠥࡺ࡯ࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡺࡻࡼ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡧࡳࡨࡹ࠯ࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡶࡩࡱ࡫࡮ࡪࡷࡰ࠳ࡷࡻ࡮࠮ࡶࡨࡷࡹࡹ࠭ࡣࡧ࡫࡭ࡳࡪ࠭ࡱࡴࡲࡼࡾࠩࡰࡺࡶ࡫ࡳࡳࠦࡦࡰࡴࠣࡥࠥࡽ࡯ࡳ࡭ࡤࡶࡴࡻ࡮ࡥ࠰ࠪ੏")
bstack11l11l11l_opy_ = bstack111lll1l1_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤࡾࡳ࡬ࠡࡨ࡬ࡰࡪ࠴࠮ࠨ੐")
bstack1ll11lll_opy_ = bstack111lll1l1_opy_ (u"ࠩࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡩࡨࡲࡪࡸࡡࡵࡧࡧࠤࡹ࡮ࡥࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠧࠧੑ")
bstack1ll111ll_opy_ = bstack111lll1l1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡰࡨࡶࡦࡺࡥࠡࡶ࡫ࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤ࡫࡯࡬ࡦ࠰ࠣࡿࢂ࠭੒")
bstack1llll1lll_opy_ = bstack111lll1l1_opy_ (u"ࠫࡊࡾࡰࡦࡥࡷࡩࡩࠦࡡࡵࠢ࡯ࡩࡦࡹࡴࠡ࠳ࠣ࡭ࡳࡶࡵࡵ࠮ࠣࡶࡪࡩࡥࡪࡸࡨࡨࠥ࠶ࠧ੓")
bstack11ll11l1_opy_ = bstack111lll1l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡩࡻࡲࡪࡰࡪࠤࡆࡶࡰࠡࡷࡳࡰࡴࡧࡤ࠯ࠢࡾࢁࠬ੔")
bstack111ll1111_opy_ = bstack111lll1l1_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡸࡴࡱࡵࡡࡥࠢࡄࡴࡵ࠴ࠠࡊࡰࡹࡥࡱ࡯ࡤࠡࡨ࡬ࡰࡪࠦࡰࡢࡶ࡫ࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡻࡾ࠰ࠪ੕")
bstack1ll1l1l11_opy_ = bstack111lll1l1_opy_ (u"ࠧࡌࡧࡼࡷࠥࡩࡡ࡯ࡰࡲࡸࠥࡩ࡯࠮ࡧࡻ࡭ࡸࡺࠠࡢࡵࠣࡥࡵࡶࠠࡷࡣ࡯ࡹࡪࡹࠬࠡࡷࡶࡩࠥࡧ࡮ࡺࠢࡲࡲࡪࠦࡰࡳࡱࡳࡩࡷࡺࡹࠡࡨࡵࡳࡲࠦࡻࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁ࠰ࠥࡶࡡࡵࡪ࠿ࡷࡹࡸࡩ࡯ࡩࡁ࠰ࠥࡩࡵࡴࡶࡲࡱࡤ࡯ࡤ࠽ࡵࡷࡶ࡮ࡴࡧ࠿࠮ࠣࡷ࡭ࡧࡲࡦࡣࡥࡰࡪࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀࢀ࠰ࠥࡵ࡮࡭ࡻࠣࠦࡵࡧࡴࡩࠤࠣࡥࡳࡪࠠࠣࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠦࠥࡩࡡ࡯ࠢࡦࡳ࠲࡫ࡸࡪࡵࡷࠤࡹࡵࡧࡦࡶ࡫ࡩࡷ࠴ࠧ੖")
bstack1l1l1l111_opy_ = bstack111lll1l1_opy_ (u"ࠨ࡝ࡌࡲࡻࡧ࡬ࡪࡦࠣࡥࡵࡶࠠࡱࡴࡲࡴࡪࡸࡴࡺ࡟ࠣࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠣࡥࡷ࡫ࠠࡼ࡫ࡧࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡰࡢࡶ࡫ࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡣࡶࡵࡷࡳࡲࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀ࠯ࠤࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁࢁ࠳ࠦࡆࡰࡴࠣࡱࡴࡸࡥࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡳࡰࡪࡧࡳࡦࠢࡹ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡺࡻࡼ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡧࡳࡨࡹ࠯ࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡡࡱࡲ࡬ࡹࡲ࠵ࡳࡦࡶ࠰ࡹࡵ࠳ࡴࡦࡵࡷࡷ࠴ࡹࡰࡦࡥ࡬ࡪࡾ࠳ࡡࡱࡲࠪ੗")
bstack1l1l1l11_opy_ = bstack111lll1l1_opy_ (u"ࠩ࡞ࡍࡳࡼࡡ࡭࡫ࡧࠤࡦࡶࡰࠡࡲࡵࡳࡵ࡫ࡲࡵࡻࡠࠤࡘࡻࡰࡱࡱࡵࡸࡪࡪࠠࡷࡣ࡯ࡹࡪࡹࠠࡰࡨࠣࡥࡵࡶࠠࡢࡴࡨࠤࡴ࡬ࠠࡼ࡫ࡧࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡰࡢࡶ࡫ࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡣࡶࡵࡷࡳࡲࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀ࠯ࠤࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁࢁ࠳ࠦࡆࡰࡴࠣࡱࡴࡸࡥࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡳࡰࡪࡧࡳࡦࠢࡹ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡺࡻࡼ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡧࡳࡨࡹ࠯ࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡡࡱࡲ࡬ࡹࡲ࠵ࡳࡦࡶ࠰ࡹࡵ࠳ࡴࡦࡵࡷࡷ࠴ࡹࡰࡦࡥ࡬ࡪࡾ࠳ࡡࡱࡲࠪ੘")
bstack1111lll_opy_ = bstack111lll1l1_opy_ (u"࡙ࠪࡸ࡯࡮ࡨࠢࡨࡼ࡮ࡹࡴࡪࡰࡪࠤࡦࡶࡰࠡ࡫ࡧࠤࢀࢃࠠࡧࡱࡵࠤ࡭ࡧࡳࡩࠢ࠽ࠤࢀࢃ࠮ࠨਖ਼")
bstack1l11_opy_ = bstack111lll1l1_opy_ (u"ࠫࡆࡶࡰࠡࡗࡳࡰࡴࡧࡤࡦࡦࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠣࡍࡉࠦ࠺ࠡࡽࢀࠫਗ਼")
bstack1lllll1l_opy_ = bstack111lll1l1_opy_ (u"࡛ࠬࡳࡪࡰࡪࠤࡆࡶࡰࠡ࠼ࠣࡿࢂ࠴ࠧਜ਼")
bstack1ll11l111_opy_ = bstack111lll1l1_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲࠦࡩࡴࠢࡱࡳࡹࠦࡳࡶࡲࡳࡳࡷࡺࡥࡥࠢࡩࡳࡷࠦࡶࡢࡰ࡬ࡰࡱࡧࠠࡱࡻࡷ࡬ࡴࡴࠠࡵࡧࡶࡸࡸ࠲ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡹ࡬ࡸ࡭ࠦࡰࡢࡴࡤࡰࡱ࡫࡬ࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠥࡃࠠ࠲ࠩੜ")
bstack1l1111ll_opy_ = bstack111lll1l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࡀࠠࡼࡿࠪ੝")
bstack11l1111_opy_ = bstack111lll1l1_opy_ (u"ࠨࡅࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡨࡲ࡯ࡴࡧࠣࡦࡷࡵࡷࡴࡧࡵ࠾ࠥࢁࡽࠨਫ਼")
bstack11l1l111_opy_ = bstack111lll1l1_opy_ (u"ࠩࡆࡳࡺࡲࡤࠡࡰࡲࡸࠥ࡭ࡥࡵࠢࡵࡩࡦࡹ࡯࡯ࠢࡩࡳࡷࠦࡢࡦࡪࡤࡺࡪࠦࡦࡦࡣࡷࡹࡷ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥ࠯ࠢࡾࢁࠬ੟")
bstack111lllll1_opy_ = bstack111lll1l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠤ࡫ࡸ࡯࡮ࠢࡤࡴ࡮ࠦࡣࡢ࡮࡯࠲ࠥࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠨ੠")
bstack111llll_opy_ = bstack111lll1l1_opy_ (u"࡚ࠫࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡪࡲࡻࠥࡨࡵࡪ࡮ࡧࠤ࡚ࡘࡌ࠭ࠢࡤࡷࠥࡨࡵࡪ࡮ࡧࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠡ࡫ࡶࠤࡳࡵࡴࠡࡷࡶࡩࡩ࠴ࠧ੡")
bstack1l1l1lll1_opy_ = bstack111lll1l1_opy_ (u"࡙ࠬࡥࡳࡸࡨࡶࠥࡹࡩࡥࡧࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠮ࡻࡾࠫࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡷࡦࡳࡥࠡࡣࡶࠤࡨࡲࡩࡦࡰࡷࠤࡸ࡯ࡤࡦࠢࡥࡹ࡮ࡲࡤࡏࡣࡰࡩ࠭ࢁࡽࠪࠩ੢")
bstack1l1ll1_opy_ = bstack111lll1l1_opy_ (u"࠭ࡖࡪࡧࡺࠤࡧࡻࡩ࡭ࡦࠣࡳࡳࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡪࡡࡴࡪࡥࡳࡦࡸࡤ࠻ࠢࡾࢁࠬ੣")
bstack11l11_opy_ = bstack111lll1l1_opy_ (u"ࠧࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡥࡨࡩࡥࡴࡵࠣࡥࠥࡶࡲࡪࡸࡤࡸࡪࠦࡤࡰ࡯ࡤ࡭ࡳࡀࠠࡼࡿࠣ࠲࡙ࠥࡥࡵࠢࡷ࡬ࡪࠦࡦࡰ࡮࡯ࡳࡼ࡯࡮ࡨࠢࡦࡳࡳ࡬ࡩࡨࠢ࡬ࡲࠥࡿ࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱࠦࡦࡪ࡮ࡨ࠾ࠥࡢ࡮࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱ࠥࡢ࡮ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰ࠿ࠦࡴࡳࡷࡨࠤࡡࡴ࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰ࠫ੤")
bstack111llll11_opy_ = bstack111lll1l1_opy_ (u"ࠨࡕࡲࡱࡪࡺࡨࡪࡰࡪࠤࡼ࡫࡮ࡵࠢࡺࡶࡴࡴࡧࠡࡹ࡫࡭ࡱ࡫ࠠࡦࡺࡨࡧࡺࡺࡩ࡯ࡩࠣ࡫ࡪࡺ࡟࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࡤ࡫ࡲࡳࡱࡵࠤ࠿ࠦࡻࡾࠩ੥")
bstack1l11l11_opy_ = bstack111lll1l1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫࡮ࡥࡡࡤࡱࡵࡲࡩࡵࡷࡧࡩࡤ࡫ࡶࡦࡰࡷࠤ࡫ࡵࡲࠡࡕࡇࡏࡘ࡫ࡴࡶࡲࠣࡿࢂࠨ੦")
bstack1ll1l111l_opy_ = bstack111lll1l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥ࡯ࡦࡢࡥࡲࡶ࡬ࡪࡶࡸࡨࡪࡥࡥࡷࡧࡱࡸࠥ࡬࡯ࡳࠢࡖࡈࡐ࡚ࡥࡴࡶࡄࡸࡹ࡫࡭ࡱࡶࡨࡨࠥࢁࡽࠣ੧")
bstack1l11l11ll_opy_ = bstack111lll1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡰࡧࡣࡦࡳࡰ࡭࡫ࡷࡹࡩ࡫࡟ࡦࡸࡨࡲࡹࠦࡦࡰࡴࠣࡗࡉࡑࡔࡦࡵࡷࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠠࡼࡿࠥ੨")
bstack11ll11ll_opy_ = bstack111lll1l1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧ࡫ࡵࡩࡤࡸࡥࡲࡷࡨࡷࡹࠦࡻࡾࠤ੩")
bstack1l111ll1l_opy_ = bstack111lll1l1_opy_ (u"ࠨࡐࡐࡕࡗࠤࡊࡼࡥ࡯ࡶࠣࡿࢂࠦࡲࡦࡵࡳࡳࡳࡹࡥࠡ࠼ࠣࡿࢂࠨ੪")
bstack1l11ll11l_opy_ = bstack111lll1l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡴࡦࡪࡩࡸࡶࡪࠦࡰࡳࡱࡻࡽࠥࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠫ੫")
bstack1l1l1l1_opy_ = bstack111lll1l1_opy_ (u"ࠨࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡪࡷࡵ࡭ࠡ࠱ࡱࡩࡽࡺ࡟ࡩࡷࡥࡷࠥࢁࡽࠨ੬")
bstack1l11l1ll1_opy_ = bstack111lll1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠠࡧࡴࡲࡱࠥ࠵࡮ࡦࡺࡷࡣ࡭ࡻࡢࡴ࠼ࠣࡿࢂ࠭੭")
bstack1llllll_opy_ = bstack111lll1l1_opy_ (u"ࠪࡒࡪࡧࡲࡦࡵࡷࠤ࡭ࡻࡢࠡࡣ࡯ࡰࡴࡩࡡࡵࡧࡧࠤ࡮ࡹ࠺ࠡࡽࢀࠫ੮")
bstack1ll1_opy_ = bstack111lll1l1_opy_ (u"ࠫࡊࡘࡒࡐࡔࠣࡍࡓࠦࡁࡍࡎࡒࡇࡆ࡚ࡅࠡࡊࡘࡆࠥࢁࡽࠨ੯")
bstack11ll11_opy_ = bstack111lll1l1_opy_ (u"ࠬࡒࡡࡵࡧࡱࡧࡾࠦ࡯ࡧࠢ࡫ࡹࡧࡀࠠࡼࡿࠣ࡭ࡸࡀࠠࡼࡿࠪੰ")
bstack1l11lll1l_opy_ = bstack111lll1l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢ࡯ࡥࡹ࡫࡮ࡤࡻࠣࡪࡴࡸࠠࡼࡿࠣ࡬ࡺࡨ࠺ࠡࡽࢀࠫੱ")
bstack11lll1l1l_opy_ = bstack111lll1l1_opy_ (u"ࠧࡉࡷࡥࠤࡺࡸ࡬ࠡࡥ࡫ࡥࡳ࡭ࡥࡥࠢࡷࡳࠥࡺࡨࡦࠢࡲࡴࡹ࡯࡭ࡢ࡮ࠣ࡬ࡺࡨ࠺ࠡࡽࢀࠫੲ")
bstack11l1lll11_opy_ = bstack111lll1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡴࡶࡴࡪ࡯ࡤࡰࠥ࡮ࡵࡣࠢࡸࡶࡱࡀࠠࡼࡿࠪੳ")
bstack11l1l1_opy_ = bstack111lll1l1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡰ࡮ࡹࡴࡴ࠼ࠣࡿࢂ࠭ੴ")
bstack1l111l1l_opy_ = bstack111lll1l1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡰࡨࡶࡦࡺࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡣࡷ࡬ࡰࡩࠦࡡࡳࡶ࡬ࡪࡦࡩࡴࡴ࠼ࠣࡿࢂ࠭ੵ")
bstack1lll111l1_opy_ = bstack111lll1l1_opy_ (u"࡚ࠫࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡰࡢࡥࠣࡪ࡮ࡲࡥࠡࡽࢀ࠲ࠥࡋࡲࡳࡱࡵࠤ࠲ࠦࡻࡾࠩ੶")
bstack1111ll1l_opy_ = bstack111lll1l1_opy_ (u"ࠬࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠥࠦࡩࡧࠪࡳࡥ࡬࡫ࠠ࠾࠿ࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠥࢁ࡜࡯ࠢࠣࠤࡹࡸࡹࡼ࡞ࡱࠤࡨࡵ࡮ࡴࡶࠣࡪࡸࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪ࡟ࠫ࡫ࡹ࡜ࠨࠫ࠾ࡠࡳࠦࠠࠡࠢࠣࡪࡸ࠴ࡡࡱࡲࡨࡲࡩࡌࡩ࡭ࡧࡖࡽࡳࡩࠨࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬࠱ࠦࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡱࡡ࡬ࡲࡩ࡫ࡸࠪࠢ࠮ࠤࠧࡀࠢࠡ࠭ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࠪࡤࡻࡦ࡯ࡴࠡࡰࡨࡻࡕࡧࡧࡦ࠴࠱ࡩࡻࡧ࡬ࡶࡣࡷࡩ࠭ࠨࠨࠪࠢࡀࡂࠥࢁࡽࠣ࠮ࠣࡠࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧ࡭ࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡆࡨࡸࡦ࡯࡬ࡴࠤࢀࡠࠬ࠯ࠩࠪ࡝ࠥ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩࠨ࡝ࠪࠢ࠮ࠤࠧ࠲࡜࡝ࡰࠥ࠭ࡡࡴࠠࠡࠢࠣࢁࡨࡧࡴࡤࡪࠫࡩࡽ࠯ࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࢂࡢ࡮ࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠬ੷")
bstack1llll1111_opy_ = bstack111lll1l1_opy_ (u"࠭࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࡟ࡲࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࡞ࡱࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࡞ࡱࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࡠࡳ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡲࡡࡶࡰࡦ࡬ࠥࡃࠠࡢࡵࡼࡲࡨࠦࠨ࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠩࠡ࠿ࡁࠤࢀࡢ࡮࡭ࡧࡷࠤࡨࡧࡰࡴ࠽࡟ࡲࡹࡸࡹࠡࡽ࡟ࡲࡨࡧࡰࡴࠢࡀࠤࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸ࠯࡜࡯ࠢࠣࢁࠥࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࠡࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻ࡝ࡰࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࡥࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠤࡼࡧࡱࡧࡴࡪࡥࡖࡔࡌࡇࡴࡳࡰࡰࡰࡨࡲࡹ࠮ࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡤࡣࡳࡷ࠮࠯ࡽࡡ࠮࡟ࡲࠥࠦࠠࠡ࠰࠱࠲ࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶࡠࡳࠦࠠࡾࠫ࡟ࡲࢂࡢ࡮࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠬ੸")
from ._version import __version__
bstack11l1l11ll_opy_ = None
CONFIG = {}
bstack1ll111_opy_ = {}
bstack1l11l111l_opy_ = {}
bstack1llll11_opy_ = None
bstack11lll11_opy_ = None
bstack11l1l111l_opy_ = None
bstack111l_opy_ = -1
bstack1ll11lll1_opy_ = bstack11l111l1_opy_
bstack1lll111ll_opy_ = 1
bstack11ll11lll_opy_ = False
bstack111lll1_opy_ = False
bstack1l1l1ll1_opy_ = bstack111lll1l1_opy_ (u"ࠧࠨ੹")
bstack111l1_opy_ = bstack111lll1l1_opy_ (u"ࠨࠩ੺")
bstack11l111l_opy_ = False
bstack11l111ll1_opy_ = True
bstack11l1_opy_ = bstack111lll1l1_opy_ (u"ࠩࠪ੻")
bstack1l111_opy_ = []
bstack111llll1_opy_ = bstack111lll1l1_opy_ (u"ࠪࠫ੼")
bstack1l111ll_opy_ = False
bstack1l1111111_opy_ = None
bstack1l111ll11_opy_ = None
bstack1llll111l_opy_ = -1
bstack1l1l1l1l1_opy_ = os.path.join(os.path.expanduser(bstack111lll1l1_opy_ (u"ࠫࢃ࠭੽")), bstack111lll1l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ੾"), bstack111lll1l1_opy_ (u"࠭࠮ࡳࡱࡥࡳࡹ࠳ࡲࡦࡲࡲࡶࡹ࠳ࡨࡦ࡮ࡳࡩࡷ࠴ࡪࡴࡱࡱࠫ੿"))
bstack1l1ll111_opy_ = []
bstack11111l_opy_ = False
bstack1l1_opy_ = None
bstack1l1l1_opy_ = None
bstack111lll_opy_ = None
bstack1l11l1_opy_ = None
bstack1lll11111_opy_ = None
bstack11l1l1ll_opy_ = None
bstack111ll_opy_ = None
bstack1l1l111l1_opy_ = None
bstack1l1ll1l_opy_ = None
bstack11111_opy_ = None
bstack11l1l_opy_ = None
bstack1ll1l11l_opy_ = None
bstack1l11l111_opy_ = None
bstack1111l11l_opy_ = None
bstack1l1l1ll_opy_ = None
bstack1llllll1_opy_ = None
bstack11llll11l_opy_ = None
bstack1llll111_opy_ = bstack111lll1l1_opy_ (u"ࠢࠣ઀")
class bstack1l111111l_opy_(threading.Thread):
  def run(self):
    self.exc = None
    try:
      self.ret = self._target(*self._args, **self._kwargs)
    except Exception as e:
      self.exc = e
  def join(self, timeout=None):
    super(bstack1l111111l_opy_, self).join(timeout)
    if self.exc:
      raise self.exc
    return self.ret
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack1ll11lll1_opy_,
                    format=bstack111lll1l1_opy_ (u"ࠨ࡞ࡱࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ઁ"),
                    datefmt=bstack111lll1l1_opy_ (u"ࠩࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫં"))
def bstack1lll1llll_opy_():
  global CONFIG
  global bstack1ll11lll1_opy_
  if bstack111lll1l1_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬઃ") in CONFIG:
    bstack1ll11lll1_opy_ = bstack11lll1ll_opy_[CONFIG[bstack111lll1l1_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭઄")]]
    logging.getLogger().setLevel(bstack1ll11lll1_opy_)
def bstack1lllllll_opy_():
  global CONFIG
  global bstack11111l_opy_
  bstack111ll1l_opy_ = bstack1l_opy_(CONFIG)
  if(bstack111lll1l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧઅ") in bstack111ll1l_opy_ and str(bstack111ll1l_opy_[bstack111lll1l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨઆ")]).lower() == bstack111lll1l1_opy_ (u"ࠧࡵࡴࡸࡩࠬઇ")):
    bstack11111l_opy_ = True
def bstack1ll11111l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1l1llll1l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack111l1111_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack111lll1l1_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡥࡲࡲ࡫࡯ࡧࡧ࡫࡯ࡩࠧઈ") == args[i].lower() or bstack111lll1l1_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡦࡪࡩࠥઉ") == args[i].lower():
      path = args[i+1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack11l1_opy_
      bstack11l1_opy_ += bstack111lll1l1_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࠠࠨઊ") + path
      return path
  return None
def bstack1llll1l_opy_():
  bstack11l11ll_opy_ = bstack111l1111_opy_()
  if bstack11l11ll_opy_ and os.path.exists(os.path.abspath(bstack11l11ll_opy_)):
    fileName = bstack11l11ll_opy_
  if bstack111lll1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨઋ") in os.environ and os.path.exists(os.path.abspath(os.environ[bstack111lll1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆࠩઌ")])) and not bstack111lll1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨઍ") in locals():
    fileName = os.environ[bstack111lll1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ઎")]
  if bstack111lll1l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡔࡡ࡮ࡧࠪએ") in locals():
    bstack111l1l1l_opy_ = os.path.abspath(fileName)
  else:
    bstack111l1l1l_opy_ = bstack111lll1l1_opy_ (u"ࠩࠪઐ")
  bstack1l111lll1_opy_ = os.getcwd()
  bstack11111111_opy_ = bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ઑ")
  bstack1l1ll11ll_opy_ = bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡦࡳ࡬ࠨ઒")
  while (not os.path.exists(bstack111l1l1l_opy_)) and bstack1l111lll1_opy_ != bstack111lll1l1_opy_ (u"ࠧࠨઓ"):
    bstack111l1l1l_opy_ = os.path.join(bstack1l111lll1_opy_, bstack11111111_opy_)
    if not os.path.exists(bstack111l1l1l_opy_):
      bstack111l1l1l_opy_ = os.path.join(bstack1l111lll1_opy_, bstack1l1ll11ll_opy_)
    if bstack1l111lll1_opy_ != os.path.dirname(bstack1l111lll1_opy_):
      bstack1l111lll1_opy_ = os.path.dirname(bstack1l111lll1_opy_)
    else:
      bstack1l111lll1_opy_ = bstack111lll1l1_opy_ (u"ࠨࠢઔ")
  if not os.path.exists(bstack111l1l1l_opy_):
    bstack11l_opy_(
      bstack111ll1l1_opy_.format(os.getcwd()))
  with open(bstack111l1l1l_opy_, bstack111lll1l1_opy_ (u"ࠧࡳࠩક")) as stream:
    try:
      config = yaml.safe_load(stream)
      return config
    except yaml.YAMLError as exc:
      bstack11l_opy_(bstack11l1l11l1_opy_.format(str(exc)))
def bstack1l1l1l11l_opy_(config):
  bstack1lllll_opy_ = bstack1l1lll1_opy_(config)
  for option in list(bstack1lllll_opy_):
    if option.lower() in bstack111ll1l1l_opy_ and option != bstack111ll1l1l_opy_[option.lower()]:
      bstack1lllll_opy_[bstack111ll1l1l_opy_[option.lower()]] = bstack1lllll_opy_[option]
      del bstack1lllll_opy_[option]
  return config
def bstack1111l1l_opy_():
  global bstack1l11l111l_opy_
  for key, bstack11lll1l1_opy_ in bstack1l11111l1_opy_.items():
    if isinstance(bstack11lll1l1_opy_, list):
      for var in bstack11lll1l1_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1l11l111l_opy_[key] = os.environ[var]
          break
    elif bstack11lll1l1_opy_ in os.environ and os.environ[bstack11lll1l1_opy_] and str(os.environ[bstack11lll1l1_opy_]).strip():
      bstack1l11l111l_opy_[key] = os.environ[bstack11lll1l1_opy_]
  if bstack111lll1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪખ") in os.environ:
    bstack1l11l111l_opy_[bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ગ")] = {}
    bstack1l11l111l_opy_[bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઘ")][bstack111lll1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ઙ")] = os.environ[bstack111lll1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧચ")]
def bstack1l1ll1l11_opy_():
  global bstack1ll111_opy_
  global bstack11l1_opy_
  for idx, val in enumerate(sys.argv):
    if idx<len(sys.argv) and bstack111lll1l1_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩછ").lower() == val.lower():
      bstack1ll111_opy_[bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫજ")] = {}
      bstack1ll111_opy_[bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬઝ")][bstack111lll1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫઞ")] = sys.argv[idx+1]
      del sys.argv[idx:idx+2]
      break
  for key, bstack1ll1l11l1_opy_ in bstack1_opy_.items():
    if isinstance(bstack1ll1l11l1_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack1ll1l11l1_opy_:
          if idx<len(sys.argv) and bstack111lll1l1_opy_ (u"ࠪ࠱࠲࠭ટ") + var.lower() == val.lower() and not key in bstack1ll111_opy_:
            bstack1ll111_opy_[key] = sys.argv[idx+1]
            bstack11l1_opy_ += bstack111lll1l1_opy_ (u"ࠫࠥ࠳࠭ࠨઠ") + var + bstack111lll1l1_opy_ (u"ࠬࠦࠧડ") + sys.argv[idx+1]
            del sys.argv[idx:idx+2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx<len(sys.argv) and bstack111lll1l1_opy_ (u"࠭࠭࠮ࠩઢ") + bstack1ll1l11l1_opy_.lower() == val.lower() and not key in bstack1ll111_opy_:
          bstack1ll111_opy_[key] = sys.argv[idx+1]
          bstack11l1_opy_ += bstack111lll1l1_opy_ (u"ࠧࠡ࠯࠰ࠫણ") + bstack1ll1l11l1_opy_ + bstack111lll1l1_opy_ (u"ࠨࠢࠪત") + sys.argv[idx+1]
          del sys.argv[idx:idx+2]
def bstack1l11llll_opy_(config):
  bstack1l11l11l1_opy_ = config.keys()
  for bstack1ll11ll_opy_, bstack11l1l1l1_opy_ in bstack11lll111_opy_.items():
    if bstack11l1l1l1_opy_ in bstack1l11l11l1_opy_:
      config[bstack1ll11ll_opy_] = config[bstack11l1l1l1_opy_]
      del config[bstack11l1l1l1_opy_]
  for bstack1ll11ll_opy_, bstack11l1l1l1_opy_ in bstack1l11ll1l1_opy_.items():
    if isinstance(bstack11l1l1l1_opy_, list):
      for bstack1l1l1l1ll_opy_ in bstack11l1l1l1_opy_:
        if bstack1l1l1l1ll_opy_ in bstack1l11l11l1_opy_:
          config[bstack1ll11ll_opy_] = config[bstack1l1l1l1ll_opy_]
          del config[bstack1l1l1l1ll_opy_]
          break
    elif bstack11l1l1l1_opy_ in bstack1l11l11l1_opy_:
        config[bstack1ll11ll_opy_] = config[bstack11l1l1l1_opy_]
        del config[bstack11l1l1l1_opy_]
  for bstack1l1l1l1ll_opy_ in list(config):
    for bstack11lll1111_opy_ in bstack11l11l11_opy_:
      if bstack1l1l1l1ll_opy_.lower() == bstack11lll1111_opy_.lower() and bstack1l1l1l1ll_opy_ != bstack11lll1111_opy_:
        config[bstack11lll1111_opy_] = config[bstack1l1l1l1ll_opy_]
        del config[bstack1l1l1l1ll_opy_]
  bstack11llll1l_opy_ = []
  if bstack111lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬથ") in config:
    bstack11llll1l_opy_ = config[bstack111lll1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭દ")]
  for platform in bstack11llll1l_opy_:
    for bstack1l1l1l1ll_opy_ in list(platform):
      for bstack11lll1111_opy_ in bstack11l11l11_opy_:
        if bstack1l1l1l1ll_opy_.lower() == bstack11lll1111_opy_.lower() and bstack1l1l1l1ll_opy_ != bstack11lll1111_opy_:
          platform[bstack11lll1111_opy_] = platform[bstack1l1l1l1ll_opy_]
          del platform[bstack1l1l1l1ll_opy_]
  for bstack1ll11ll_opy_, bstack11l1l1l1_opy_ in bstack1l11ll1l1_opy_.items():
    for platform in bstack11llll1l_opy_:
      if isinstance(bstack11l1l1l1_opy_, list):
        for bstack1l1l1l1ll_opy_ in bstack11l1l1l1_opy_:
          if bstack1l1l1l1ll_opy_ in platform:
            platform[bstack1ll11ll_opy_] = platform[bstack1l1l1l1ll_opy_]
            del platform[bstack1l1l1l1ll_opy_]
            break
      elif bstack11l1l1l1_opy_ in platform:
        platform[bstack1ll11ll_opy_] = platform[bstack11l1l1l1_opy_]
        del platform[bstack11l1l1l1_opy_]
  for bstack111l1ll11_opy_ in bstack1ll1l11ll_opy_:
    if bstack111l1ll11_opy_ in config:
      if not bstack1ll1l11ll_opy_[bstack111l1ll11_opy_] in config:
        config[bstack1ll1l11ll_opy_[bstack111l1ll11_opy_]] = {}
      config[bstack1ll1l11ll_opy_[bstack111l1ll11_opy_]].update(config[bstack111l1ll11_opy_])
      del config[bstack111l1ll11_opy_]
  for platform in bstack11llll1l_opy_:
    for bstack111l1ll11_opy_ in bstack1ll1l11ll_opy_:
      if bstack111l1ll11_opy_ in list(platform):
        if not bstack1ll1l11ll_opy_[bstack111l1ll11_opy_] in platform:
          platform[bstack1ll1l11ll_opy_[bstack111l1ll11_opy_]] = {}
        platform[bstack1ll1l11ll_opy_[bstack111l1ll11_opy_]].update(platform[bstack111l1ll11_opy_])
        del platform[bstack111l1ll11_opy_]
  config = bstack1l1l1l11l_opy_(config)
  return config
def bstack111l1ll1l_opy_(config):
  global bstack111l1_opy_
  if bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨધ") in config and str(config[bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩન")]).lower() != bstack111lll1l1_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ઩"):
    if not bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫપ") in config:
      config[bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬફ")] = {}
    if not bstack111lll1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫબ") in config[bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧભ")]:
      bstack11l1111l1_opy_ = datetime.datetime.now()
      bstack1ll11ll1l_opy_ = bstack11l1111l1_opy_.strftime(bstack111lll1l1_opy_ (u"ࠫࠪࡪ࡟ࠦࡤࡢࠩࡍࠫࡍࠨમ"))
      hostname = socket.gethostname()
      bstack1llll1ll_opy_ = bstack111lll1l1_opy_ (u"ࠬ࠭ય").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack111lll1l1_opy_ (u"࠭ࡻࡾࡡࡾࢁࡤࢁࡽࠨર").format(bstack1ll11ll1l_opy_, hostname, bstack1llll1ll_opy_)
      config[bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ઱")][bstack111lll1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪલ")] = identifier
    bstack111l1_opy_ = config[bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ળ")][bstack111lll1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ઴")]
  return config
def bstack1ll1111ll_opy_():
  if (
    isinstance(os.getenv(bstack111lll1l1_opy_ (u"ࠫࡏࡋࡎࡌࡋࡑࡗࡤ࡛ࡒࡍࠩવ")), str) and len(os.getenv(bstack111lll1l1_opy_ (u"ࠬࡐࡅࡏࡍࡌࡒࡘࡥࡕࡓࡎࠪશ"))) > 0
  ) or (
    isinstance(os.getenv(bstack111lll1l1_opy_ (u"࠭ࡊࡆࡐࡎࡍࡓ࡙࡟ࡉࡑࡐࡉࠬષ")), str) and len(os.getenv(bstack111lll1l1_opy_ (u"ࠧࡋࡇࡑࡏࡎࡔࡓࡠࡊࡒࡑࡊ࠭સ"))) > 0
  ):
    return os.getenv(bstack111lll1l1_opy_ (u"ࠨࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠧહ"), 0)
  if str(os.getenv(bstack111lll1l1_opy_ (u"ࠩࡆࡍࠬ઺"))).lower() == bstack111lll1l1_opy_ (u"ࠪࡸࡷࡻࡥࠨ઻") and str(os.getenv(bstack111lll1l1_opy_ (u"ࠫࡈࡏࡒࡄࡎࡈࡇࡎ઼࠭"))).lower() == bstack111lll1l1_opy_ (u"ࠬࡺࡲࡶࡧࠪઽ"):
    return os.getenv(bstack111lll1l1_opy_ (u"࠭ࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࠩા"), 0)
  if str(os.getenv(bstack111lll1l1_opy_ (u"ࠧࡄࡋࠪિ"))).lower() == bstack111lll1l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭ી") and str(os.getenv(bstack111lll1l1_opy_ (u"ࠩࡗࡖࡆ࡜ࡉࡔࠩુ"))).lower() == bstack111lll1l1_opy_ (u"ࠪࡸࡷࡻࡥࠨૂ"):
    return os.getenv(bstack111lll1l1_opy_ (u"࡙ࠫࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠪૃ"), 0)
  if str(os.getenv(bstack111lll1l1_opy_ (u"ࠬࡉࡉࠨૄ"))).lower() == bstack111lll1l1_opy_ (u"࠭ࡴࡳࡷࡨࠫૅ") and str(os.getenv(bstack111lll1l1_opy_ (u"ࠧࡄࡋࡢࡒࡆࡓࡅࠨ૆"))).lower() == bstack111lll1l1_opy_ (u"ࠨࡥࡲࡨࡪࡹࡨࡪࡲࠪે"):
    return 0 # bstack11l11l111_opy_ bstack1lll11_opy_ not set build number env
  if os.getenv(bstack111lll1l1_opy_ (u"ࠩࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠬૈ")) and os.getenv(bstack111lll1l1_opy_ (u"ࠪࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙࠭ૉ")):
    return os.getenv(bstack111lll1l1_opy_ (u"ࠫࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗ࠭૊"), 0)
  if str(os.getenv(bstack111lll1l1_opy_ (u"ࠬࡉࡉࠨો"))).lower() == bstack111lll1l1_opy_ (u"࠭ࡴࡳࡷࡨࠫૌ") and str(os.getenv(bstack111lll1l1_opy_ (u"ࠧࡅࡔࡒࡒࡊ્࠭"))).lower() == bstack111lll1l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭૎"):
    return os.getenv(bstack111lll1l1_opy_ (u"ࠩࡇࡖࡔࡔࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠧ૏"), 0)
  if str(os.getenv(bstack111lll1l1_opy_ (u"ࠪࡇࡎ࠭ૐ"))).lower() == bstack111lll1l1_opy_ (u"ࠫࡹࡸࡵࡦࠩ૑") and str(os.getenv(bstack111lll1l1_opy_ (u"࡙ࠬࡅࡎࡃࡓࡌࡔࡘࡅࠨ૒"))).lower() == bstack111lll1l1_opy_ (u"࠭ࡴࡳࡷࡨࠫ૓"):
    return os.getenv(bstack111lll1l1_opy_ (u"ࠧࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡊࡆࠪ૔"), 0)
  if str(os.getenv(bstack111lll1l1_opy_ (u"ࠨࡅࡌࠫ૕"))).lower() == bstack111lll1l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ૖") and str(os.getenv(bstack111lll1l1_opy_ (u"ࠪࡋࡎ࡚ࡌࡂࡄࡢࡇࡎ࠭૗"))).lower() == bstack111lll1l1_opy_ (u"ࠫࡹࡸࡵࡦࠩ૘"):
    return os.getenv(bstack111lll1l1_opy_ (u"ࠬࡉࡉࡠࡌࡒࡆࡤࡏࡄࠨ૙"), 0)
  if str(os.getenv(bstack111lll1l1_opy_ (u"࠭ࡃࡊࠩ૚"))).lower() == bstack111lll1l1_opy_ (u"ࠧࡵࡴࡸࡩࠬ૛") and str(os.getenv(bstack111lll1l1_opy_ (u"ࠨࡄࡘࡍࡑࡊࡋࡊࡖࡈࠫ૜"))).lower() == bstack111lll1l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ૝"):
    return os.getenv(bstack111lll1l1_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠬ૞"), 0)
  if str(os.getenv(bstack111lll1l1_opy_ (u"࡙ࠫࡌ࡟ࡃࡗࡌࡐࡉ࠭૟"))).lower() == bstack111lll1l1_opy_ (u"ࠬࡺࡲࡶࡧࠪૠ"):
    return os.getenv(bstack111lll1l1_opy_ (u"࠭ࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉ࠭ૡ"), 0)
  return -1
def bstack111l1l1_opy_(bstack1111llll_opy_):
  global CONFIG
  if not bstack111lll1l1_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩૢ") in CONFIG[bstack111lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪૣ")]:
    return
  CONFIG[bstack111lll1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૤")] = CONFIG[bstack111lll1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૥")].replace(
    bstack111lll1l1_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭૦"),
    str(bstack1111llll_opy_)
  )
def bstack111l111l_opy_():
  global CONFIG
  if not bstack111lll1l1_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫ૧") in CONFIG[bstack111lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૨")]:
    return
  bstack11l1111l1_opy_ = datetime.datetime.now()
  bstack1ll11ll1l_opy_ = bstack11l1111l1_opy_.strftime(bstack111lll1l1_opy_ (u"ࠧࠦࡦ࠰ࠩࡧ࠳ࠥࡉ࠼ࠨࡑࠬ૩"))
  CONFIG[bstack111lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૪")] = CONFIG[bstack111lll1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૫")].replace(
    bstack111lll1l1_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩ૬"),
    bstack1ll11ll1l_opy_
  )
def bstack1111lll1_opy_():
  global CONFIG
  if bstack111lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૭") in CONFIG and not bool(CONFIG[bstack111lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૮")]):
    del CONFIG[bstack111lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૯")]
    return
  if not bstack111lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૰") in CONFIG:
    CONFIG[bstack111lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૱")] = bstack111lll1l1_opy_ (u"ࠩࠦࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬ૲")
  if bstack111lll1l1_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩ૳") in CONFIG[bstack111lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૴")]:
    bstack111l111l_opy_()
    os.environ[bstack111lll1l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ૵")] = CONFIG[bstack111lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૶")]
  if not bstack111lll1l1_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩ૷") in CONFIG[bstack111lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૸")]:
    return
  bstack1111llll_opy_ = bstack111lll1l1_opy_ (u"ࠩࠪૹ")
  bstack1lll11l1l_opy_ = bstack1ll1111ll_opy_()
  if bstack1lll11l1l_opy_ != -1:
    bstack1111llll_opy_ = bstack111lll1l1_opy_ (u"ࠪࡇࡎࠦࠧૺ") + str(bstack1lll11l1l_opy_)
  if bstack1111llll_opy_ == bstack111lll1l1_opy_ (u"ࠫࠬૻ"):
    bstack11ll111l_opy_ = bstack1l1lll11l_opy_(CONFIG[bstack111lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨૼ")])
    if bstack11ll111l_opy_ != -1:
      bstack1111llll_opy_ = str(bstack11ll111l_opy_)
  if bstack1111llll_opy_:
    bstack111l1l1_opy_(bstack1111llll_opy_)
    os.environ[bstack111lll1l1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪ૽")] = CONFIG[bstack111lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૾")]
def bstack11ll1l1l_opy_(bstack1lll1ll1_opy_, bstack1l11l_opy_, path):
  bstack1ll11_opy_ = {
    bstack111lll1l1_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૿"): bstack1l11l_opy_
  }
  if os.path.exists(path):
    bstack1ll11llll_opy_ = json.load(open(path, bstack111lll1l1_opy_ (u"ࠩࡵࡦࠬ଀")))
  else:
    bstack1ll11llll_opy_ = {}
  bstack1ll11llll_opy_[bstack1lll1ll1_opy_] = bstack1ll11_opy_
  with open(path, bstack111lll1l1_opy_ (u"ࠥࡻ࠰ࠨଁ")) as outfile:
    json.dump(bstack1ll11llll_opy_, outfile)
def bstack1l1lll11l_opy_(bstack1lll1ll1_opy_):
  bstack1lll1ll1_opy_ = str(bstack1lll1ll1_opy_)
  bstack11l111lll_opy_ = os.path.join(os.path.expanduser(bstack111lll1l1_opy_ (u"ࠫࢃ࠭ଂ")), bstack111lll1l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬଃ"))
  try:
    if not os.path.exists(bstack11l111lll_opy_):
      os.makedirs(bstack11l111lll_opy_)
    file_path = os.path.join(os.path.expanduser(bstack111lll1l1_opy_ (u"࠭ࡾࠨ଄")), bstack111lll1l1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧଅ"), bstack111lll1l1_opy_ (u"ࠨ࠰ࡥࡹ࡮ࡲࡤ࠮ࡰࡤࡱࡪ࠳ࡣࡢࡥ࡫ࡩ࠳ࡰࡳࡰࡰࠪଆ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack111lll1l1_opy_ (u"ࠩࡺࠫଇ")):
        pass
      with open(file_path, bstack111lll1l1_opy_ (u"ࠥࡻ࠰ࠨଈ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack111lll1l1_opy_ (u"ࠫࡷ࠭ଉ")) as bstack111ll11l_opy_:
      bstack1lllllll1_opy_ = json.load(bstack111ll11l_opy_)
    if bstack1lll1ll1_opy_ in bstack1lllllll1_opy_:
      bstack1lll1lll_opy_ = bstack1lllllll1_opy_[bstack1lll1ll1_opy_][bstack111lll1l1_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩଊ")]
      bstack11l111111_opy_ = int(bstack1lll1lll_opy_) + 1
      bstack11ll1l1l_opy_(bstack1lll1ll1_opy_, bstack11l111111_opy_, file_path)
      return bstack11l111111_opy_
    else:
      bstack11ll1l1l_opy_(bstack1lll1ll1_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1l1111ll_opy_.format(str(e)))
    return -1
def bstack1lllll1ll_opy_(config):
  if not config[bstack111lll1l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨଋ")] or not config[bstack111lll1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪଌ")]:
    return True
  else:
    return False
def bstack11lllll11_opy_(config):
  if bstack111lll1l1_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧ଍") in config:
    del(config[bstack111lll1l1_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨ଎")])
    return False
  if bstack1l1llll1l_opy_() < version.parse(bstack111lll1l1_opy_ (u"ࠪ࠷࠳࠺࠮࠱ࠩଏ")):
    return False
  if bstack1l1llll1l_opy_() >= version.parse(bstack111lll1l1_opy_ (u"ࠫ࠹࠴࠱࠯࠷ࠪଐ")):
    return True
  if bstack111lll1l1_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬ଑") in config and config[bstack111lll1l1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭଒")] == False:
    return False
  else:
    return True
def bstack11ll_opy_(config, index = 0):
  global bstack11l111l_opy_
  bstack11ll1111_opy_ = {}
  caps = bstack1l111l1l1_opy_ + bstack1l111111_opy_
  if bstack11l111l_opy_:
    caps += bstack11111l11_opy_
  for key in config:
    if key in caps + [bstack111lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଓ")]:
      continue
    bstack11ll1111_opy_[key] = config[key]
  if bstack111lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଔ") in config:
    for bstack1l1l1l_opy_ in config[bstack111lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬକ")][index]:
      if bstack1l1l1l_opy_ in caps + [bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଖ"), bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬଗ")]:
        continue
      bstack11ll1111_opy_[bstack1l1l1l_opy_] = config[bstack111lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଘ")][index][bstack1l1l1l_opy_]
  bstack11ll1111_opy_[bstack111lll1l1_opy_ (u"࠭ࡨࡰࡵࡷࡒࡦࡳࡥࠨଙ")] = socket.gethostname()
  if bstack111lll1l1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨଚ") in bstack11ll1111_opy_:
    del(bstack11ll1111_opy_[bstack111lll1l1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩଛ")])
  return bstack11ll1111_opy_
def bstack1ll1lllll_opy_(config):
  global bstack11l111l_opy_
  bstack11lll1ll1_opy_ = {}
  caps = bstack1l111111_opy_
  if bstack11l111l_opy_:
    caps+= bstack11111l11_opy_
  for key in caps:
    if key in config:
      bstack11lll1ll1_opy_[key] = config[key]
  return bstack11lll1ll1_opy_
def bstack1l111l11_opy_(bstack11ll1111_opy_, bstack11lll1ll1_opy_):
  bstack11l11l1l_opy_ = {}
  for key in bstack11ll1111_opy_.keys():
    if key in bstack11lll111_opy_:
      bstack11l11l1l_opy_[bstack11lll111_opy_[key]] = bstack11ll1111_opy_[key]
    else:
      bstack11l11l1l_opy_[key] = bstack11ll1111_opy_[key]
  for key in bstack11lll1ll1_opy_:
    if key in bstack11lll111_opy_:
      bstack11l11l1l_opy_[bstack11lll111_opy_[key]] = bstack11lll1ll1_opy_[key]
    else:
      bstack11l11l1l_opy_[key] = bstack11lll1ll1_opy_[key]
  return bstack11l11l1l_opy_
def bstack11l11llll_opy_(config, index = 0):
  global bstack11l111l_opy_
  config = copy.deepcopy(config)
  caps = {}
  bstack11lll1ll1_opy_ = bstack1ll1lllll_opy_(config)
  bstack111l111_opy_ = bstack1l111111_opy_
  bstack111l111_opy_ += bstack1ll1l1lll_opy_
  if bstack11l111l_opy_:
    bstack111l111_opy_ += bstack11111l11_opy_
  if bstack111lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଜ") in config:
    if bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଝ") in config[bstack111lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଞ")][index]:
      caps[bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪଟ")] = config[bstack111lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩଠ")][index][bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬଡ")]
    if bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଢ") in config[bstack111lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଣ")][index]:
      caps[bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫତ")] = str(config[bstack111lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଥ")][index][bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଦ")])
    bstack11l1l11l_opy_ = {}
    for bstack1111l111_opy_ in bstack111l111_opy_:
      if bstack1111l111_opy_ in config[bstack111lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩଧ")][index]:
        if bstack1111l111_opy_ == bstack111lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩନ"):
          bstack11l1l11l_opy_[bstack1111l111_opy_] = str(config[bstack111lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ଩")][index][bstack1111l111_opy_] * 1.0)
        else:
          bstack11l1l11l_opy_[bstack1111l111_opy_] = config[bstack111lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬପ")][index][bstack1111l111_opy_]
        del(config[bstack111lll1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଫ")][index][bstack1111l111_opy_])
    bstack11lll1ll1_opy_ = update(bstack11lll1ll1_opy_, bstack11l1l11l_opy_)
  bstack11ll1111_opy_ = bstack11ll_opy_(config, index)
  for bstack1l1l1l1ll_opy_ in bstack1l111111_opy_ + [bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩବ"), bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଭ")]:
    if bstack1l1l1l1ll_opy_ in bstack11ll1111_opy_:
      bstack11lll1ll1_opy_[bstack1l1l1l1ll_opy_] = bstack11ll1111_opy_[bstack1l1l1l1ll_opy_]
      del(bstack11ll1111_opy_[bstack1l1l1l1ll_opy_])
  if bstack11lllll11_opy_(config):
    bstack11ll1111_opy_[bstack111lll1l1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ମ")] = True
    caps.update(bstack11lll1ll1_opy_)
    caps[bstack111lll1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨଯ")] = bstack11ll1111_opy_
  else:
    bstack11ll1111_opy_[bstack111lll1l1_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨର")] = False
    caps.update(bstack1l111l11_opy_(bstack11ll1111_opy_, bstack11lll1ll1_opy_))
    if bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ଱") in caps:
      caps[bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫଲ")] = caps[bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଳ")]
      del(caps[bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ଴")])
    if bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧଵ") in caps:
      caps[bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩଶ")] = caps[bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଷ")]
      del(caps[bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪସ")])
  return caps
def bstack111lll1ll_opy_():
  global bstack111llll1_opy_
  if bstack1l1llll1l_opy_() <= version.parse(bstack111lll1l1_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪହ")):
    if bstack111llll1_opy_ != bstack111lll1l1_opy_ (u"ࠫࠬ଺"):
      return bstack111lll1l1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨ଻") + bstack111llll1_opy_ + bstack111lll1l1_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤ଼ࠥ")
    return bstack1l1111l_opy_
  if  bstack111llll1_opy_ != bstack111lll1l1_opy_ (u"ࠧࠨଽ"):
    return bstack111lll1l1_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥା") + bstack111llll1_opy_ + bstack111lll1l1_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥି")
  return bstack1l1l1ll1l_opy_
def bstack11lllll_opy_(options):
  return hasattr(options, bstack111lll1l1_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫୀ"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1ll1lll1_opy_(options, bstack111ll1l11_opy_):
  for bstack1l1lll11_opy_ in bstack111ll1l11_opy_:
    if bstack1l1lll11_opy_ in [bstack111lll1l1_opy_ (u"ࠫࡦࡸࡧࡴࠩୁ"), bstack111lll1l1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩୂ")]:
      next
    if bstack1l1lll11_opy_ in options._experimental_options:
      options._experimental_options[bstack1l1lll11_opy_]= update(options._experimental_options[bstack1l1lll11_opy_], bstack111ll1l11_opy_[bstack1l1lll11_opy_])
    else:
      options.add_experimental_option(bstack1l1lll11_opy_, bstack111ll1l11_opy_[bstack1l1lll11_opy_])
  if bstack111lll1l1_opy_ (u"࠭ࡡࡳࡩࡶࠫୃ") in bstack111ll1l11_opy_:
    for arg in bstack111ll1l11_opy_[bstack111lll1l1_opy_ (u"ࠧࡢࡴࡪࡷࠬୄ")]:
      options.add_argument(arg)
    del(bstack111ll1l11_opy_[bstack111lll1l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭୅")])
  if bstack111lll1l1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭୆") in bstack111ll1l11_opy_:
    for ext in bstack111ll1l11_opy_[bstack111lll1l1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧେ")]:
      options.add_extension(ext)
    del(bstack111ll1l11_opy_[bstack111lll1l1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨୈ")])
def bstack1l1l11ll_opy_(options, bstack1llll1_opy_):
  if bstack111lll1l1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ୉") in bstack1llll1_opy_:
    for bstack1l1l1l1l_opy_ in bstack1llll1_opy_[bstack111lll1l1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ୊")]:
      if bstack1l1l1l1l_opy_ in options._preferences:
        options._preferences[bstack1l1l1l1l_opy_] = update(options._preferences[bstack1l1l1l1l_opy_], bstack1llll1_opy_[bstack111lll1l1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ୋ")][bstack1l1l1l1l_opy_])
      else:
        options.set_preference(bstack1l1l1l1l_opy_, bstack1llll1_opy_[bstack111lll1l1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧୌ")][bstack1l1l1l1l_opy_])
  if bstack111lll1l1_opy_ (u"ࠩࡤࡶ࡬ࡹ୍ࠧ") in bstack1llll1_opy_:
    for arg in bstack1llll1_opy_[bstack111lll1l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ୎")]:
      options.add_argument(arg)
def bstack1llll11l_opy_(options, bstack1l1ll1l1l_opy_):
  if bstack111lll1l1_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬ୏") in bstack1l1ll1l1l_opy_:
    options.use_webview(bool(bstack1l1ll1l1l_opy_[bstack111lll1l1_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭୐")]))
  bstack1ll1lll1_opy_(options, bstack1l1ll1l1l_opy_)
def bstack1l1lll1ll_opy_(options, bstack11l11l_opy_):
  for bstack111ll11l1_opy_ in bstack11l11l_opy_:
    if bstack111ll11l1_opy_ in [bstack111lll1l1_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪ୑"), bstack111lll1l1_opy_ (u"ࠧࡢࡴࡪࡷࠬ୒")]:
      next
    options.set_capability(bstack111ll11l1_opy_, bstack11l11l_opy_[bstack111ll11l1_opy_])
  if bstack111lll1l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭୓") in bstack11l11l_opy_:
    for arg in bstack11l11l_opy_[bstack111lll1l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ୔")]:
      options.add_argument(arg)
  if bstack111lll1l1_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧ୕") in bstack11l11l_opy_:
    options.use_technology_preview(bool(bstack11l11l_opy_[bstack111lll1l1_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨୖ")]))
def bstack1l1l111_opy_(options, bstack1l1ll1lll_opy_):
  for bstack1l11lll_opy_ in bstack1l1ll1lll_opy_:
    if bstack1l11lll_opy_ in [bstack111lll1l1_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩୗ"), bstack111lll1l1_opy_ (u"࠭ࡡࡳࡩࡶࠫ୘")]:
      next
    options._options[bstack1l11lll_opy_] = bstack1l1ll1lll_opy_[bstack1l11lll_opy_]
  if bstack111lll1l1_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୙") in bstack1l1ll1lll_opy_:
    for bstack1ll1111l_opy_ in bstack1l1ll1lll_opy_[bstack111lll1l1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୚")]:
      options.bstack1lll1ll1l_opy_(
          bstack1ll1111l_opy_, bstack1l1ll1lll_opy_[bstack111lll1l1_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୛")][bstack1ll1111l_opy_])
  if bstack111lll1l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଡ଼") in bstack1l1ll1lll_opy_:
    for arg in bstack1l1ll1lll_opy_[bstack111lll1l1_opy_ (u"ࠫࡦࡸࡧࡴࠩଢ଼")]:
      options.add_argument(arg)
def bstack11ll1_opy_(options, caps):
  if not hasattr(options, bstack111lll1l1_opy_ (u"ࠬࡑࡅ࡚ࠩ୞")):
    return
  if options.KEY == bstack111lll1l1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫୟ") and options.KEY in caps:
    bstack1ll1lll1_opy_(options, caps[bstack111lll1l1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬୠ")])
  elif options.KEY == bstack111lll1l1_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ୡ") and options.KEY in caps:
    bstack1l1l11ll_opy_(options, caps[bstack111lll1l1_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧୢ")])
  elif options.KEY == bstack111lll1l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫୣ") and options.KEY in caps:
    bstack1l1lll1ll_opy_(options, caps[bstack111lll1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬ୤")])
  elif options.KEY == bstack111lll1l1_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭୥") and options.KEY in caps:
    bstack1llll11l_opy_(options, caps[bstack111lll1l1_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ୦")])
  elif options.KEY == bstack111lll1l1_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭୧") and options.KEY in caps:
    bstack1l1l111_opy_(options, caps[bstack111lll1l1_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ୨")])
def bstack11lll1lll_opy_(caps):
  global bstack11l111l_opy_
  if bstack11l111l_opy_:
    if bstack1ll11111l_opy_() < version.parse(bstack111lll1l1_opy_ (u"ࠩ࠵࠲࠸࠴࠰ࠨ୩")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack111lll1l1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪ୪")
    if bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ୫") in caps:
      browser = caps[bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ୬")]
    elif bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧ୭") in caps:
      browser = caps[bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ୮")]
    browser = str(browser).lower()
    if browser == bstack111lll1l1_opy_ (u"ࠨ࡫ࡳ࡬ࡴࡴࡥࠨ୯") or browser == bstack111lll1l1_opy_ (u"ࠩ࡬ࡴࡦࡪࠧ୰"):
      browser = bstack111lll1l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪୱ")
    if browser == bstack111lll1l1_opy_ (u"ࠫࡸࡧ࡭ࡴࡷࡱ࡫ࠬ୲"):
      browser = bstack111lll1l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ୳")
    if browser not in [bstack111lll1l1_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭୴"), bstack111lll1l1_opy_ (u"ࠧࡦࡦࡪࡩࠬ୵"), bstack111lll1l1_opy_ (u"ࠨ࡫ࡨࠫ୶"), bstack111lll1l1_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩ୷"), bstack111lll1l1_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫ୸")]:
      return None
    try:
      package = bstack111lll1l1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡾࢁ࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭୹").format(browser)
      name = bstack111lll1l1_opy_ (u"ࠬࡕࡰࡵ࡫ࡲࡲࡸ࠭୺")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11lllll_opy_(options):
        return None
      for bstack1l1l1l1ll_opy_ in caps.keys():
        options.set_capability(bstack1l1l1l1ll_opy_, caps[bstack1l1l1l1ll_opy_])
      bstack11ll1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack111111l1_opy_(options, bstack11l11lll1_opy_):
  if not bstack11lllll_opy_(options):
    return
  for bstack1l1l1l1ll_opy_ in bstack11l11lll1_opy_.keys():
    if bstack1l1l1l1ll_opy_ in bstack1ll1l1lll_opy_:
      next
    if bstack1l1l1l1ll_opy_ in options._caps and type(options._caps[bstack1l1l1l1ll_opy_]) in [dict, list]:
      options._caps[bstack1l1l1l1ll_opy_] = update(options._caps[bstack1l1l1l1ll_opy_], bstack11l11lll1_opy_[bstack1l1l1l1ll_opy_])
    else:
      options.set_capability(bstack1l1l1l1ll_opy_, bstack11l11lll1_opy_[bstack1l1l1l1ll_opy_])
  bstack11ll1_opy_(options, bstack11l11lll1_opy_)
  if bstack111lll1l1_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬ୻") in options._caps:
    if options._caps[bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ୼")] and options._caps[bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭୽")].lower() != bstack111lll1l1_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪ୾"):
      del options._caps[bstack111lll1l1_opy_ (u"ࠪࡱࡴࢀ࠺ࡥࡧࡥࡹ࡬࡭ࡥࡳࡃࡧࡨࡷ࡫ࡳࡴࠩ୿")]
def bstack1l11111ll_opy_(proxy_config):
  if bstack111lll1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ஀") in proxy_config:
    proxy_config[bstack111lll1l1_opy_ (u"ࠬࡹࡳ࡭ࡒࡵࡳࡽࡿࠧ஁")] = proxy_config[bstack111lll1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪஂ")]
    del(proxy_config[bstack111lll1l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫஃ")])
  if bstack111lll1l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ஄") in proxy_config and proxy_config[bstack111lll1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬஅ")].lower() != bstack111lll1l1_opy_ (u"ࠪࡨ࡮ࡸࡥࡤࡶࠪஆ"):
    proxy_config[bstack111lll1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧஇ")] = bstack111lll1l1_opy_ (u"ࠬࡳࡡ࡯ࡷࡤࡰࠬஈ")
  if bstack111lll1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࡆࡻࡴࡰࡥࡲࡲ࡫࡯ࡧࡖࡴ࡯ࠫஉ") in proxy_config:
    proxy_config[bstack111lll1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪஊ")] = bstack111lll1l1_opy_ (u"ࠨࡲࡤࡧࠬ஋")
  return proxy_config
def bstack1l11l1111_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack111lll1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨ஌") in config:
    return proxy
  config[bstack111lll1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩ஍")] = bstack1l11111ll_opy_(config[bstack111lll1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪஎ")])
  if proxy == None:
    proxy = Proxy(config[bstack111lll1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫஏ")])
  return proxy
def bstack111lll11l_opy_(self):
  global CONFIG
  global bstack11111_opy_
  try:
    proxy = bstack1l1l1lll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack111lll1l1_opy_ (u"࠭࠮ࡱࡣࡦࠫஐ")):
        proxies = bstack1l1ll11l_opy_(proxy, bstack111lll1ll_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll11l11_opy_ = proxies.popitem()
          if bstack111lll1l1_opy_ (u"ࠢ࠻࠱࠲ࠦ஑") in bstack1ll11l11_opy_:
            return bstack1ll11l11_opy_
          else:
            return bstack111lll1l1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤஒ") + bstack1ll11l11_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack111lll1l1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨஓ").format(str(e)))
  return bstack11111_opy_(self)
def bstack11lll1l11_opy_():
  global CONFIG
  return bstack111lll1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ஔ") in CONFIG or bstack111lll1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨக") in CONFIG
def bstack1l1l1lll_opy_(config):
  if not bstack11lll1l11_opy_():
    return
  if config.get(bstack111lll1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ஖")):
    return config.get(bstack111lll1l1_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ஗"))
  if config.get(bstack111lll1l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ஘")):
    return config.get(bstack111lll1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬங"))
def bstack1l1l111l_opy_(url):
  try:
      result = urlparse(url)
      return all([result.scheme, result.netloc])
  except:
      return False
def bstack11ll11111_opy_(bstack1111l1l1_opy_, bstack1111l11_opy_):
  from pypac import get_pac
  from pypac import PACSession
  from pypac.parser import PACFile
  import socket
  if os.path.isfile(bstack1111l1l1_opy_):
    with open(bstack1111l1l1_opy_) as f:
      pac = PACFile(f.read())
  elif bstack1l1l111l_opy_(bstack1111l1l1_opy_):
    pac = get_pac(url=bstack1111l1l1_opy_)
  else:
    raise Exception(bstack111lll1l1_opy_ (u"ࠩࡓࡥࡨࠦࡦࡪ࡮ࡨࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠿ࠦࡻࡾࠩச").format(bstack1111l1l1_opy_))
  session = PACSession(pac)
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((bstack111lll1l1_opy_ (u"ࠥ࠼࠳࠾࠮࠹࠰࠻ࠦ஛"), 80))
    bstack1lllll1_opy_ = s.getsockname()[0]
    s.close()
  except:
    bstack1lllll1_opy_ = bstack111lll1l1_opy_ (u"ࠫ࠵࠴࠰࠯࠲࠱࠴ࠬஜ")
  proxy_url = session.get_pac().find_proxy_for_url(bstack1111l11_opy_, bstack1lllll1_opy_)
  return proxy_url
def bstack1l1ll11l_opy_(bstack1111l1l1_opy_, bstack1111l11_opy_):
  proxies = {}
  global bstack1l1111l1_opy_
  if bstack111lll1l1_opy_ (u"ࠬࡖࡁࡄࡡࡓࡖࡔ࡞࡙ࠨ஝") in globals():
    return bstack1l1111l1_opy_
  try:
    proxy = bstack11ll11111_opy_(bstack1111l1l1_opy_,bstack1111l11_opy_)
    if bstack111lll1l1_opy_ (u"ࠨࡄࡊࡔࡈࡇ࡙ࠨஞ") in proxy:
      proxies = {}
    elif bstack111lll1l1_opy_ (u"ࠢࡉࡖࡗࡔࠧட") in proxy or bstack111lll1l1_opy_ (u"ࠣࡊࡗࡘࡕ࡙ࠢ஠") in proxy or bstack111lll1l1_opy_ (u"ࠤࡖࡓࡈࡑࡓࠣ஡") in proxy:
      bstack11lll111l_opy_ = proxy.split(bstack111lll1l1_opy_ (u"ࠥࠤࠧ஢"))
      if bstack111lll1l1_opy_ (u"ࠦ࠿࠵࠯ࠣண") in bstack111lll1l1_opy_ (u"ࠧࠨத").join(bstack11lll111l_opy_[1:]):
        proxies = {
          bstack111lll1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ஥"): bstack111lll1l1_opy_ (u"ࠢࠣ஦").join(bstack11lll111l_opy_[1:])
        }
      else:
        proxies = {
          bstack111lll1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧ஧") : str(bstack11lll111l_opy_[0]).lower()+ bstack111lll1l1_opy_ (u"ࠤ࠽࠳࠴ࠨந") + bstack111lll1l1_opy_ (u"ࠥࠦன").join(bstack11lll111l_opy_[1:])
        }
    elif bstack111lll1l1_opy_ (u"ࠦࡕࡘࡏ࡙࡛ࠥப") in proxy:
      bstack11lll111l_opy_ = proxy.split(bstack111lll1l1_opy_ (u"ࠧࠦࠢ஫"))
      if bstack111lll1l1_opy_ (u"ࠨ࠺࠰࠱ࠥ஬") in bstack111lll1l1_opy_ (u"ࠢࠣ஭").join(bstack11lll111l_opy_[1:]):
        proxies = {
          bstack111lll1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧம"): bstack111lll1l1_opy_ (u"ࠤࠥய").join(bstack11lll111l_opy_[1:])
        }
      else:
        proxies = {
          bstack111lll1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩர"): bstack111lll1l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧற") + bstack111lll1l1_opy_ (u"ࠧࠨல").join(bstack11lll111l_opy_[1:])
        }
    else:
      proxies = {
        bstack111lll1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬள"): proxy
      }
  except Exception as e:
    logger.error(bstack1lll111l1_opy_.format(bstack1111l1l1_opy_, str(e)))
  bstack1l1111l1_opy_ = proxies
  return proxies
def bstack1ll11ll1_opy_(config, bstack1111l11_opy_):
  proxy = bstack1l1l1lll_opy_(config)
  proxies = {}
  if config.get(bstack111lll1l1_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪழ")) or config.get(bstack111lll1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬவ")):
    if proxy.endswith(bstack111lll1l1_opy_ (u"ࠩ࠱ࡴࡦࡩࠧஶ")):
      proxies = bstack1l1ll11l_opy_(proxy,bstack1111l11_opy_)
    else:
      proxies = {
        bstack111lll1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩஷ"): proxy
      }
  return proxies
def bstack11l111_opy_():
  return bstack11lll1l11_opy_() and bstack1l1llll1l_opy_() >= version.parse(bstack11l1l1ll1_opy_)
def bstack1l1lll1_opy_(config):
  bstack1lllll_opy_ = {}
  if bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨஸ") in config:
    bstack1lllll_opy_ =  config[bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩஹ")]
  if bstack111lll1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ஺") in config:
    bstack1lllll_opy_ = config[bstack111lll1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭஻")]
  proxy = bstack1l1l1lll_opy_(config)
  if proxy:
    if proxy.endswith(bstack111lll1l1_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭஼")) and os.path.isfile(proxy):
      bstack1lllll_opy_[bstack111lll1l1_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬ஽")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack111lll1l1_opy_ (u"ࠪ࠲ࡵࡧࡣࠨா")):
        proxies = bstack1ll11ll1_opy_(config, bstack111lll1ll_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll11l11_opy_ = proxies.popitem()
          if bstack111lll1l1_opy_ (u"ࠦ࠿࠵࠯ࠣி") in bstack1ll11l11_opy_:
            parsed_url = urlparse(bstack1ll11l11_opy_)
          else:
            parsed_url = urlparse(protocol + bstack111lll1l1_opy_ (u"ࠧࡀ࠯࠰ࠤீ") + bstack1ll11l11_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1lllll_opy_[bstack111lll1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩு")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1lllll_opy_[bstack111lll1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖ࡯ࡳࡶࠪூ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1lllll_opy_[bstack111lll1l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫ௃")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1lllll_opy_[bstack111lll1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬ௄")] = str(parsed_url.password)
  return bstack1lllll_opy_
def bstack1l_opy_(config):
  if bstack111lll1l1_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨ௅") in config:
    return config[bstack111lll1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩெ")]
  return {}
def bstack1llll1l1l_opy_(caps):
  global bstack111l1_opy_
  if bstack111lll1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ே") in caps:
    caps[bstack111lll1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧை")][bstack111lll1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭௉")] = True
    if bstack111l1_opy_:
      caps[bstack111lll1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩொ")][bstack111lll1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫோ")] = bstack111l1_opy_
  else:
    caps[bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࠨௌ")] = True
    if bstack111l1_opy_:
      caps[bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ்ࠬ")] = bstack111l1_opy_
def bstack11l11ll1l_opy_():
  global CONFIG
  if bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ௎") in CONFIG and CONFIG[bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ௏")]:
    bstack1lllll_opy_ = bstack1l1lll1_opy_(CONFIG)
    bstack111l1llll_opy_(CONFIG[bstack111lll1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪௐ")], bstack1lllll_opy_)
def bstack111l1llll_opy_(key, bstack1lllll_opy_):
  global bstack11l1l11ll_opy_
  logger.info(bstack1ll111ll1_opy_)
  try:
    bstack11l1l11ll_opy_ = Local()
    bstack1l1l11lll_opy_ = {bstack111lll1l1_opy_ (u"ࠨ࡭ࡨࡽࠬ௑"): key}
    bstack1l1l11lll_opy_.update(bstack1lllll_opy_)
    logger.debug(bstack111llllll_opy_.format(str(bstack1l1l11lll_opy_)))
    bstack11l1l11ll_opy_.start(**bstack1l1l11lll_opy_)
    if bstack11l1l11ll_opy_.isRunning():
      logger.info(bstack11l1l1lll_opy_)
  except Exception as e:
    bstack11l_opy_(bstack1l111l1ll_opy_.format(str(e)))
def bstack1l1llll11_opy_():
  global bstack11l1l11ll_opy_
  if bstack11l1l11ll_opy_.isRunning():
    logger.info(bstack11l11l1l1_opy_)
    bstack11l1l11ll_opy_.stop()
  bstack11l1l11ll_opy_ = None
def bstack11lll1l_opy_(bstack11_opy_=[]):
  global CONFIG
  bstack1l11l1l_opy_ = []
  bstack11lll_opy_ = [bstack111lll1l1_opy_ (u"ࠩࡲࡷࠬ௒"), bstack111lll1l1_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭௓"), bstack111lll1l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ௔"), bstack111lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ௕"), bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ௖"), bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨௗ")]
  try:
    for err in bstack11_opy_:
      bstack1ll11l_opy_ = {}
      for k in bstack11lll_opy_:
        val = CONFIG[bstack111lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௘")][int(err[bstack111lll1l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ௙")])].get(k)
        if val:
          bstack1ll11l_opy_[k] = val
      bstack1ll11l_opy_[bstack111lll1l1_opy_ (u"ࠪࡸࡪࡹࡴࡴࠩ௚")] = {
        err[bstack111lll1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ௛")]: err[bstack111lll1l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ௜")]
      }
      bstack1l11l1l_opy_.append(bstack1ll11l_opy_)
  except Exception as e:
    logger.debug(bstack111lll1l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡲࡶࡲࡧࡴࡵ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࡀࠠࠨ௝") +str(e))
  finally:
    return bstack1l11l1l_opy_
def bstack11l1lllll_opy_():
  global bstack1llll111_opy_
  global bstack1l111_opy_
  global bstack1l1ll111_opy_
  if bstack1llll111_opy_:
    logger.warning(bstack11l11_opy_.format(str(bstack1llll111_opy_)))
  logger.info(bstack1ll1ll11_opy_)
  global bstack11l1l11ll_opy_
  if bstack11l1l11ll_opy_:
    bstack1l1llll11_opy_()
  try:
    for driver in bstack1l111_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack111ll111_opy_)
  bstack1l11ll11_opy_()
  if len(bstack1l1ll111_opy_) > 0:
    message = bstack11lll1l_opy_(bstack1l1ll111_opy_)
    bstack1l11ll11_opy_(message)
  else:
    bstack1l11ll11_opy_()
def bstack11ll1l11l_opy_(self, *args):
  logger.error(bstack11l1l1l1l_opy_)
  bstack11l1lllll_opy_()
  sys.exit(1)
def bstack11l_opy_(err):
  logger.critical(bstack1ll1ll1_opy_.format(str(err)))
  bstack1l11ll11_opy_(bstack1ll1ll1_opy_.format(str(err)))
  atexit.unregister(bstack11l1lllll_opy_)
  sys.exit(1)
def bstack1ll111l11_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l11ll11_opy_(message)
  atexit.unregister(bstack11l1lllll_opy_)
  sys.exit(1)
def bstack1lll11ll_opy_():
  global CONFIG
  global bstack1ll111_opy_
  global bstack1l11l111l_opy_
  global bstack11l111ll1_opy_
  CONFIG = bstack1llll1l_opy_()
  bstack1111l1l_opy_()
  bstack1l1ll1l11_opy_()
  CONFIG = bstack1l11llll_opy_(CONFIG)
  update(CONFIG, bstack1l11l111l_opy_)
  update(CONFIG, bstack1ll111_opy_)
  CONFIG = bstack111l1ll1l_opy_(CONFIG)
  if bstack111lll1l1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ௞") in CONFIG and str(CONFIG[bstack111lll1l1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ௟")]).lower() == bstack111lll1l1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ௠"):
    bstack11l111ll1_opy_ = False
  if (bstack111lll1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௡") in CONFIG and bstack111lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௢") in bstack1ll111_opy_) or (bstack111lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௣") in CONFIG and bstack111lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௤") not in bstack1l11l111l_opy_):
    if os.getenv(bstack111lll1l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ௥")):
      CONFIG[bstack111lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ௦")] = os.getenv(bstack111lll1l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭௧"))
    else:
      bstack1111lll1_opy_()
  elif (bstack111lll1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௨") not in CONFIG and bstack111lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௩") in CONFIG) or (bstack111lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௪") in bstack1l11l111l_opy_ and bstack111lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௫") not in bstack1ll111_opy_):
    del(CONFIG[bstack111lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ௬")])
  if bstack1lllll1ll_opy_(CONFIG):
    bstack11l_opy_(bstack1lll1l1_opy_)
  bstack1lll1l1ll_opy_()
  bstack1ll1l1l1_opy_()
  if bstack11l111l_opy_:
    CONFIG[bstack111lll1l1_opy_ (u"ࠨࡣࡳࡴࠬ௭")] = bstack111ll11_opy_(CONFIG)
    logger.info(bstack1lllll1l_opy_.format(CONFIG[bstack111lll1l1_opy_ (u"ࠩࡤࡴࡵ࠭௮")]))
def bstack1ll1l1l1_opy_():
  global CONFIG
  global bstack11l111l_opy_
  if bstack111lll1l1_opy_ (u"ࠪࡥࡵࡶࠧ௯") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1ll111l11_opy_(e, bstack1ll_opy_)
    bstack11l111l_opy_ = True
def bstack111ll11_opy_(config):
  bstack1ll11l1_opy_ = bstack111lll1l1_opy_ (u"ࠫࠬ௰")
  app = config[bstack111lll1l1_opy_ (u"ࠬࡧࡰࡱࠩ௱")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1l1ll11l1_opy_:
      if os.path.exists(app):
        bstack1ll11l1_opy_ = bstack111l1ll1_opy_(config, app)
      elif bstack1lll1l11l_opy_(app):
        bstack1ll11l1_opy_ = app
      else:
        bstack11l_opy_(bstack111ll1111_opy_.format(app))
    else:
      if bstack1lll1l11l_opy_(app):
        bstack1ll11l1_opy_ = app
      elif os.path.exists(app):
        bstack1ll11l1_opy_ = bstack111l1ll1_opy_(app)
      else:
        bstack11l_opy_(bstack1l1l1l11_opy_)
  else:
    if len(app) > 2:
      bstack11l_opy_(bstack1ll1l1l11_opy_)
    elif len(app) == 2:
      if bstack111lll1l1_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ௲") in app and bstack111lll1l1_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ௳") in app:
        if os.path.exists(app[bstack111lll1l1_opy_ (u"ࠨࡲࡤࡸ࡭࠭௴")]):
          bstack1ll11l1_opy_ = bstack111l1ll1_opy_(config, app[bstack111lll1l1_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ௵")], app[bstack111lll1l1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭௶")])
        else:
          bstack11l_opy_(bstack111ll1111_opy_.format(app))
      else:
        bstack11l_opy_(bstack1ll1l1l11_opy_)
    else:
      for key in app:
        if key in bstack1llll11ll_opy_:
          if key == bstack111lll1l1_opy_ (u"ࠫࡵࡧࡴࡩࠩ௷"):
            if os.path.exists(app[key]):
              bstack1ll11l1_opy_ = bstack111l1ll1_opy_(config, app[key])
            else:
              bstack11l_opy_(bstack111ll1111_opy_.format(app))
          else:
            bstack1ll11l1_opy_ = app[key]
        else:
          bstack11l_opy_(bstack1l1l1l111_opy_)
  return bstack1ll11l1_opy_
def bstack1lll1l11l_opy_(bstack1ll11l1_opy_):
  import re
  bstack1lll1ll11_opy_ = re.compile(bstack111lll1l1_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧ௸"))
  bstack111_opy_ = re.compile(bstack111lll1l1_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮࠴ࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥ௹"))
  if bstack111lll1l1_opy_ (u"ࠧࡣࡵ࠽࠳࠴࠭௺") in bstack1ll11l1_opy_ or re.fullmatch(bstack1lll1ll11_opy_, bstack1ll11l1_opy_) or re.fullmatch(bstack111_opy_, bstack1ll11l1_opy_):
    return True
  else:
    return False
def bstack111l1ll1_opy_(config, path, bstack11ll111l1_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack111lll1l1_opy_ (u"ࠨࡴࡥࠫ௻")).read()).hexdigest()
  bstack11l1lll1l_opy_ = bstack111ll1_opy_(md5_hash)
  bstack1ll11l1_opy_ = None
  if bstack11l1lll1l_opy_:
    logger.info(bstack1111lll_opy_.format(bstack11l1lll1l_opy_, md5_hash))
    return bstack11l1lll1l_opy_
  bstack1lll111l_opy_ = MultipartEncoder(
    fields={
        bstack111lll1l1_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧ௼"): (os.path.basename(path), open(os.path.abspath(path), bstack111lll1l1_opy_ (u"ࠪࡶࡧ࠭௽")), bstack111lll1l1_opy_ (u"ࠫࡹ࡫ࡸࡵ࠱ࡳࡰࡦ࡯࡮ࠨ௾")),
        bstack111lll1l1_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ௿"): bstack11ll111l1_opy_
    }
  )
  response = requests.post(bstack1ll1ll1ll_opy_, data=bstack1lll111l_opy_,
                         headers={bstack111lll1l1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬఀ"): bstack1lll111l_opy_.content_type}, auth=(config[bstack111lll1l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩఁ")], config[bstack111lll1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫం")]))
  try:
    res = json.loads(response.text)
    bstack1ll11l1_opy_ = res[bstack111lll1l1_opy_ (u"ࠩࡤࡴࡵࡥࡵࡳ࡮ࠪః")]
    logger.info(bstack1l11_opy_.format(bstack1ll11l1_opy_))
    bstack1l1l1ll11_opy_(md5_hash, bstack1ll11l1_opy_)
  except ValueError as err:
    bstack11l_opy_(bstack11ll11l1_opy_.format(str(err)))
  return bstack1ll11l1_opy_
def bstack1lll1l1ll_opy_():
  global CONFIG
  global bstack1lll111ll_opy_
  bstack11111l1l_opy_ = 0
  bstack1l11l1ll_opy_ = 1
  if bstack111lll1l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪఄ") in CONFIG:
    bstack1l11l1ll_opy_ = CONFIG[bstack111lll1l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫఅ")]
  if bstack111lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఆ") in CONFIG:
    bstack11111l1l_opy_ = len(CONFIG[bstack111lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩఇ")])
  bstack1lll111ll_opy_ = int(bstack1l11l1ll_opy_) * int(bstack11111l1l_opy_)
def bstack111ll1_opy_(md5_hash):
  bstack111lll11_opy_ = os.path.join(os.path.expanduser(bstack111lll1l1_opy_ (u"ࠧࡿࠩఈ")), bstack111lll1l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨఉ"), bstack111lll1l1_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪఊ"))
  if os.path.exists(bstack111lll11_opy_):
    bstack1l11llll1_opy_ = json.load(open(bstack111lll11_opy_,bstack111lll1l1_opy_ (u"ࠪࡶࡧ࠭ఋ")))
    if md5_hash in bstack1l11llll1_opy_:
      bstack1ll1111l1_opy_ = bstack1l11llll1_opy_[md5_hash]
      bstack11l11111l_opy_ = datetime.datetime.now()
      bstack1l1l1111l_opy_ = datetime.datetime.strptime(bstack1ll1111l1_opy_[bstack111lll1l1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧఌ")], bstack111lll1l1_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩ఍"))
      if (bstack11l11111l_opy_ - bstack1l1l1111l_opy_).days > 60:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1ll1111l1_opy_[bstack111lll1l1_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫఎ")]):
        return None
      return bstack1ll1111l1_opy_[bstack111lll1l1_opy_ (u"ࠧࡪࡦࠪఏ")]
  else:
    return None
def bstack1l1l1ll11_opy_(md5_hash, bstack1ll11l1_opy_):
  bstack11l111lll_opy_ = os.path.join(os.path.expanduser(bstack111lll1l1_opy_ (u"ࠨࢀࠪఐ")), bstack111lll1l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ఑"))
  if not os.path.exists(bstack11l111lll_opy_):
    os.makedirs(bstack11l111lll_opy_)
  bstack111lll11_opy_ = os.path.join(os.path.expanduser(bstack111lll1l1_opy_ (u"ࠪࢂࠬఒ")), bstack111lll1l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఓ"), bstack111lll1l1_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ఔ"))
  bstack1l1111l11_opy_ = {
    bstack111lll1l1_opy_ (u"࠭ࡩࡥࠩక"): bstack1ll11l1_opy_,
    bstack111lll1l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪఖ"): datetime.datetime.strftime(datetime.datetime.now(), bstack111lll1l1_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬగ")),
    bstack111lll1l1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧఘ"): str(__version__)
  }
  if os.path.exists(bstack111lll11_opy_):
    bstack1l11llll1_opy_ = json.load(open(bstack111lll11_opy_,bstack111lll1l1_opy_ (u"ࠪࡶࡧ࠭ఙ")))
  else:
    bstack1l11llll1_opy_ = {}
  bstack1l11llll1_opy_[md5_hash] = bstack1l1111l11_opy_
  with open(bstack111lll11_opy_, bstack111lll1l1_opy_ (u"ࠦࡼ࠱ࠢచ")) as outfile:
    json.dump(bstack1l11llll1_opy_, outfile)
def bstack11l111l1l_opy_(self):
  return
def bstack11l11ll11_opy_(self):
  return
def bstack1ll111111_opy_(self):
  from selenium.webdriver.remote.webdriver import WebDriver
  WebDriver.quit(self)
def bstack1l1lll111_opy_(self, command_executor,
        desired_capabilities=None, browser_profile=None, proxy=None,
        keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1llll11_opy_
  global bstack111l_opy_
  global bstack11l1l111l_opy_
  global bstack11ll11lll_opy_
  global bstack111lll1_opy_
  global bstack1l1l1ll1_opy_
  global bstack1l1_opy_
  global bstack1l111_opy_
  global bstack1llll111l_opy_
  CONFIG[bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧఛ")] = str(bstack1l1l1ll1_opy_) + str(__version__)
  command_executor = bstack111lll1ll_opy_()
  logger.debug(bstack11ll11ll1_opy_.format(command_executor))
  proxy = bstack1l11l1111_opy_(CONFIG, proxy)
  bstack1ll111l1l_opy_ = 0 if bstack111l_opy_ < 0 else bstack111l_opy_
  if bstack11ll11lll_opy_ is True:
    bstack1ll111l1l_opy_ = int(multiprocessing.current_process().name)
  if bstack111lll1_opy_ is True:
    bstack1ll111l1l_opy_ = int(str(threading.current_thread().name).split(bstack111lll1l1_opy_ (u"࠭࡟ࡣࡵࡷࡥࡨࡱ࡟ࠨజ"))[0])
  bstack11l11lll1_opy_ = bstack11l11llll_opy_(CONFIG, bstack1ll111l1l_opy_)
  logger.debug(bstack11l11l1ll_opy_.format(str(bstack11l11lll1_opy_)))
  if bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫఝ") in CONFIG and CONFIG[bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬఞ")]:
    bstack1llll1l1l_opy_(bstack11l11lll1_opy_)
  if desired_capabilities:
    bstack1lll1ll_opy_ = bstack1l11llll_opy_(desired_capabilities)
    bstack1lll1ll_opy_[bstack111lll1l1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩట")] = bstack11lllll11_opy_(CONFIG)
    bstack1l111l_opy_ = bstack11l11llll_opy_(bstack1lll1ll_opy_)
    if bstack1l111l_opy_:
      bstack11l11lll1_opy_ = update(bstack1l111l_opy_, bstack11l11lll1_opy_)
    desired_capabilities = None
  if options:
    bstack111111l1_opy_(options, bstack11l11lll1_opy_)
  if not options:
    options = bstack11lll1lll_opy_(bstack11l11lll1_opy_)
  if proxy and bstack1l1llll1l_opy_() >= version.parse(bstack111lll1l1_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪఠ")):
    options.proxy(proxy)
  if options and bstack1l1llll1l_opy_() >= version.parse(bstack111lll1l1_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪడ")):
    desired_capabilities = None
  if (
      not options and not desired_capabilities
  ) or (
      bstack1l1llll1l_opy_() < version.parse(bstack111lll1l1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫఢ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack11l11lll1_opy_)
  logger.info(bstack1l1l11111_opy_)
  if bstack1l1llll1l_opy_() >= version.parse(bstack111lll1l1_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭ణ")):
    bstack1l1_opy_(self, command_executor=command_executor,
          options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1llll1l_opy_() >= version.parse(bstack111lll1l1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭త")):
    bstack1l1_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities, options=options,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1llll1l_opy_() >= version.parse(bstack111lll1l1_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨథ")):
    bstack1l1_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack1l1_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive)
  try:
    bstack1l111lll_opy_ = bstack111lll1l1_opy_ (u"ࠩࠪద")
    if bstack1l1llll1l_opy_() >= version.parse(bstack111lll1l1_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࡤ࠴ࠫధ")):
      bstack1l111lll_opy_ = self.caps.get(bstack111lll1l1_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦన"))
    else:
      bstack1l111lll_opy_ = self.capabilities.get(bstack111lll1l1_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧ఩"))
    if bstack1l111lll_opy_:
      if bstack1l1llll1l_opy_() <= version.parse(bstack111lll1l1_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ప")):
        self.command_executor._url = bstack111lll1l1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣఫ") + bstack111llll1_opy_ + bstack111lll1l1_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧబ")
      else:
        self.command_executor._url = bstack111lll1l1_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦభ") + bstack1l111lll_opy_ + bstack111lll1l1_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦమ")
      logger.debug(bstack11lll1l1l_opy_.format(bstack1l111lll_opy_))
    else:
      logger.debug(bstack11l1lll11_opy_.format(bstack111lll1l1_opy_ (u"ࠦࡔࡶࡴࡪ࡯ࡤࡰࠥࡎࡵࡣࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧయ")))
  except Exception as e:
    logger.debug(bstack11l1lll11_opy_.format(e))
  if bstack111lll1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫర") in bstack1l1l1ll1_opy_:
    bstack1l1111_opy_(bstack111l_opy_, bstack1llll111l_opy_)
  bstack1llll11_opy_ = self.session_id
  if bstack111lll1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ఱ") in bstack1l1l1ll1_opy_:
    current_name = threading.current_thread().name
    new_name = current_name + bstack111lll1l1_opy_ (u"ࠧࡠࡤࡶࡸࡦࡩ࡫ࡠࠩల") + self.session_id
    threading.current_thread().name = new_name
  bstack1l111_opy_.append(self)
  if bstack111lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫళ") in CONFIG and bstack111lll1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧఴ") in CONFIG[bstack111lll1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭వ")][bstack1ll111l1l_opy_]:
    bstack11l1l111l_opy_ = CONFIG[bstack111lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧశ")][bstack1ll111l1l_opy_][bstack111lll1l1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪష")]
  logger.debug(bstack1ll1l1_opy_.format(bstack1llll11_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    def bstack11llllll1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1l111ll_opy_
      if(bstack111lll1l1_opy_ (u"ࠨࡩ࡯ࡦࡨࡼ࠳ࡰࡳࠣస") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack111lll1l1_opy_ (u"ࠧࡿࠩహ")), bstack111lll1l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ఺"), bstack111lll1l1_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ఻")), bstack111lll1l1_opy_ (u"ࠪࡻ఼ࠬ")) as fp:
          fp.write(bstack111lll1l1_opy_ (u"ࠦࠧఽ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack111lll1l1_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢా")))):
          with open(args[1], bstack111lll1l1_opy_ (u"࠭ࡲࠨి")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack111lll1l1_opy_ (u"ࠧࡢࡵࡼࡲࡨࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡡࡱࡩࡼࡖࡡࡨࡧࠫࡧࡴࡴࡴࡦࡺࡷ࠰ࠥࡶࡡࡨࡧࠣࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮࠭ీ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1111ll1l_opy_)
            lines.insert(1, bstack1llll1111_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack111lll1l1_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥు")), bstack111lll1l1_opy_ (u"ࠩࡺࠫూ")) as bstack1lll1l1l1_opy_:
              bstack1lll1l1l1_opy_.writelines(lines)
        CONFIG[bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬృ")] = str(bstack1l1l1ll1_opy_) + str(__version__)
        bstack1ll111l1l_opy_ = 0 if bstack111l_opy_ < 0 else bstack111l_opy_
        if bstack11ll11lll_opy_ is True:
          bstack1ll111l1l_opy_ = int(threading.current_thread().getName())
        CONFIG[bstack111lll1l1_opy_ (u"ࠦࡺࡹࡥࡘ࠵ࡆࠦౄ")] = False
        CONFIG[bstack111lll1l1_opy_ (u"ࠧ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ౅")] = True
        bstack11l11lll1_opy_ = bstack11l11llll_opy_(CONFIG, bstack1ll111l1l_opy_)
        logger.debug(bstack11l11l1ll_opy_.format(str(bstack11l11lll1_opy_)))
        if CONFIG[bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪె")]:
          bstack1llll1l1l_opy_(bstack11l11lll1_opy_)
        if bstack111lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪే") in CONFIG and bstack111lll1l1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ై") in CONFIG[bstack111lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ౉")][bstack1ll111l1l_opy_]:
          bstack11l1l111l_opy_ = CONFIG[bstack111lll1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ొ")][bstack1ll111l1l_opy_][bstack111lll1l1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩో")]
        args.append(os.path.join(os.path.expanduser(bstack111lll1l1_opy_ (u"ࠬࢄࠧౌ")), bstack111lll1l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ్࠭"), bstack111lll1l1_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩ౎")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack11l11lll1_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack111lll1l1_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥ౏"))
      bstack1l111ll_opy_ = True
      return bstack1l11l111_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack1ll111lll_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1llll11_opy_
    global bstack111l_opy_
    global bstack11l1l111l_opy_
    global bstack11ll11lll_opy_
    global bstack1l1l1ll1_opy_
    global bstack1l1_opy_
    CONFIG[bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ౐")] = str(bstack1l1l1ll1_opy_) + str(__version__)
    bstack1ll111l1l_opy_ = 0 if bstack111l_opy_ < 0 else bstack111l_opy_
    if bstack11ll11lll_opy_ is True:
      bstack1ll111l1l_opy_ = int(threading.current_thread().getName())
    CONFIG[bstack111lll1l1_opy_ (u"ࠥ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ౑")] = True
    bstack11l11lll1_opy_ = bstack11l11llll_opy_(CONFIG, bstack1ll111l1l_opy_)
    logger.debug(bstack11l11l1ll_opy_.format(str(bstack11l11lll1_opy_)))
    if CONFIG[bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ౒")]:
      bstack1llll1l1l_opy_(bstack11l11lll1_opy_)
    if bstack111lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ౓") in CONFIG and bstack111lll1l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ౔") in CONFIG[bstack111lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵౕࠪ")][bstack1ll111l1l_opy_]:
      bstack11l1l111l_opy_ = CONFIG[bstack111lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶౖࠫ")][bstack1ll111l1l_opy_][bstack111lll1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ౗")]
    import urllib
    import json
    bstack11ll111_opy_ = bstack111lll1l1_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬౘ") + urllib.parse.quote(json.dumps(bstack11l11lll1_opy_))
    browser = self.connect(bstack11ll111_opy_)
    return browser
except Exception as e:
    pass
def bstack1l11ll_opy_():
    global bstack1l111ll_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1ll111lll_opy_
        bstack1l111ll_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack11llllll1_opy_
      bstack1l111ll_opy_ = True
    except Exception as e:
      pass
def bstack11ll11l11_opy_(context, bstack11ll11l1l_opy_):
  try:
    context.page.evaluate(bstack111lll1l1_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧౙ"), bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠩౚ")+ json.dumps(bstack11ll11l1l_opy_) + bstack111lll1l1_opy_ (u"ࠨࡽࡾࠤ౛"))
  except Exception as e:
    logger.debug(bstack111lll1l1_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢࡾࢁࠧ౜"), e)
def bstack1l1llll1_opy_(context, message, level):
  try:
    context.page.evaluate(bstack111lll1l1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤౝ"), bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ౞") + json.dumps(message) + bstack111lll1l1_opy_ (u"ࠪ࠰ࠧࡲࡥࡷࡧ࡯ࠦ࠿࠭౟") + json.dumps(level) + bstack111lll1l1_opy_ (u"ࠫࢂࢃࠧౠ"))
  except Exception as e:
    logger.debug(bstack111lll1l1_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠥࢁࡽࠣౡ"), e)
def bstack1llll1l11_opy_(context, status, message = bstack111lll1l1_opy_ (u"ࠨࠢౢ")):
  try:
    if(status == bstack111lll1l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢౣ")):
      context.page.evaluate(bstack111lll1l1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ౤"), bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡴࡨࡥࡸࡵ࡮ࠣ࠼ࠪ౥") + json.dumps(bstack111lll1l1_opy_ (u"ࠥࡗࡨ࡫࡮ࡢࡴ࡬ࡳࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࠧ౦") + str(message)) + bstack111lll1l1_opy_ (u"ࠫ࠱ࠨࡳࡵࡣࡷࡹࡸࠨ࠺ࠨ౧") + json.dumps(status) + bstack111lll1l1_opy_ (u"ࠧࢃࡽࠣ౨"))
    else:
      context.page.evaluate(bstack111lll1l1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢ౩"), bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡳࡵࡣࡷࡹࡸࠨ࠺ࠨ౪") + json.dumps(status) + bstack111lll1l1_opy_ (u"ࠣࡿࢀࠦ౫"))
  except Exception as e:
    logger.debug(bstack111lll1l1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡿࢂࠨ౬"), e)
def bstack1lllll11l_opy_(self, url):
  global bstack1ll1l11l_opy_
  try:
    bstack1llllll1l_opy_(url)
  except Exception as err:
    logger.debug(bstack111llll11_opy_.format(str(err)))
  try:
    bstack1ll1l11l_opy_(self, url)
  except Exception as e:
    try:
      bstack1111l1_opy_ = str(e)
      if any(err_msg in bstack1111l1_opy_ for err_msg in bstack111l1l_opy_):
        bstack1llllll1l_opy_(url, True)
    except Exception as err:
      logger.debug(bstack111llll11_opy_.format(str(err)))
    raise e
def bstack11lllllll_opy_(self):
  global bstack1l111ll11_opy_
  bstack1l111ll11_opy_ = self
  return
def bstack1ll1l1ll1_opy_(self):
  global bstack1l1111111_opy_
  bstack1l1111111_opy_ = self
  return
def bstack11l1ll1l1_opy_(self, test):
  global CONFIG
  global bstack1l1111111_opy_
  global bstack1l111ll11_opy_
  global bstack1llll11_opy_
  global bstack11lll11_opy_
  global bstack11l1l111l_opy_
  global bstack1l1l1_opy_
  global bstack111lll_opy_
  global bstack1l11l1_opy_
  global bstack1l111_opy_
  try:
    if not bstack1llll11_opy_:
      with open(os.path.join(os.path.expanduser(bstack111lll1l1_opy_ (u"ࠪࢂࠬ౭")), bstack111lll1l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ౮"), bstack111lll1l1_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧ౯"))) as f:
        bstack1ll1l_opy_ = json.loads(bstack111lll1l1_opy_ (u"ࠨࡻࠣ౰") + f.read().strip() + bstack111lll1l1_opy_ (u"ࠧࠣࡺࠥ࠾ࠥࠨࡹࠣࠩ౱") + bstack111lll1l1_opy_ (u"ࠣࡿࠥ౲"))
        bstack1llll11_opy_ = bstack1ll1l_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1l111_opy_:
    for driver in bstack1l111_opy_:
      if bstack1llll11_opy_ == driver.session_id:
        if test:
          bstack11l111l11_opy_ = str(test.data)
        if not bstack11111l_opy_ and bstack11l111l11_opy_:
          bstack1l11111_opy_ = {
            bstack111lll1l1_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ౳"): bstack111lll1l1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ౴"),
            bstack111lll1l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ౵"): {
              bstack111lll1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ౶"): bstack11l111l11_opy_
            }
          }
          bstack1lll1111l_opy_ = bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ౷").format(json.dumps(bstack1l11111_opy_))
          driver.execute_script(bstack1lll1111l_opy_)
        if bstack11lll11_opy_:
          bstack11l1ll11l_opy_ = {
            bstack111lll1l1_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ౸"): bstack111lll1l1_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪ౹"),
            bstack111lll1l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ౺"): {
              bstack111lll1l1_opy_ (u"ࠪࡨࡦࡺࡡࠨ౻"): bstack11l111l11_opy_ + bstack111lll1l1_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭౼"),
              bstack111lll1l1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ౽"): bstack111lll1l1_opy_ (u"࠭ࡩ࡯ࡨࡲࠫ౾")
            }
          }
          bstack1l11111_opy_ = {
            bstack111lll1l1_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ౿"): bstack111lll1l1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫಀ"),
            bstack111lll1l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬಁ"): {
              bstack111lll1l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪಂ"): bstack111lll1l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫಃ")
            }
          }
          if bstack11lll11_opy_.status == bstack111lll1l1_opy_ (u"ࠬࡖࡁࡔࡕࠪ಄"):
            bstack11ll1l1l1_opy_ = bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫಅ").format(json.dumps(bstack11l1ll11l_opy_))
            driver.execute_script(bstack11ll1l1l1_opy_)
            bstack1lll1111l_opy_ = bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬಆ").format(json.dumps(bstack1l11111_opy_))
            driver.execute_script(bstack1lll1111l_opy_)
          elif bstack11lll11_opy_.status == bstack111lll1l1_opy_ (u"ࠨࡈࡄࡍࡑ࠭ಇ"):
            reason = bstack111lll1l1_opy_ (u"ࠤࠥಈ")
            bstack1l111l11l_opy_ = bstack11l111l11_opy_ + bstack111lll1l1_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠫಉ")
            if bstack11lll11_opy_.message:
              reason = str(bstack11lll11_opy_.message)
              bstack1l111l11l_opy_ = bstack1l111l11l_opy_ + bstack111lll1l1_opy_ (u"ࠫࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠫಊ") + reason
            bstack11l1ll11l_opy_[bstack111lll1l1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨಋ")] = {
              bstack111lll1l1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬಌ"): bstack111lll1l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭಍"),
              bstack111lll1l1_opy_ (u"ࠨࡦࡤࡸࡦ࠭ಎ"): bstack1l111l11l_opy_
            }
            bstack1l11111_opy_[bstack111lll1l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬಏ")] = {
              bstack111lll1l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪಐ"): bstack111lll1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ಑"),
              bstack111lll1l1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬಒ"): reason
            }
            bstack11ll1l1l1_opy_ = bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫಓ").format(json.dumps(bstack11l1ll11l_opy_))
            driver.execute_script(bstack11ll1l1l1_opy_)
            bstack1lll1111l_opy_ = bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬಔ").format(json.dumps(bstack1l11111_opy_))
            driver.execute_script(bstack1lll1111l_opy_)
  elif bstack1llll11_opy_:
    try:
      data = {}
      bstack11l111l11_opy_ = None
      if test:
        bstack11l111l11_opy_ = str(test.data)
      if not bstack11111l_opy_ and bstack11l111l11_opy_:
        data[bstack111lll1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ಕ")] = bstack11l111l11_opy_
      if bstack11lll11_opy_:
        if bstack11lll11_opy_.status == bstack111lll1l1_opy_ (u"ࠩࡓࡅࡘ࡙ࠧಖ"):
          data[bstack111lll1l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪಗ")] = bstack111lll1l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫಘ")
        elif bstack11lll11_opy_.status == bstack111lll1l1_opy_ (u"ࠬࡌࡁࡊࡎࠪಙ"):
          data[bstack111lll1l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ಚ")] = bstack111lll1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧಛ")
          if bstack11lll11_opy_.message:
            data[bstack111lll1l1_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨಜ")] = str(bstack11lll11_opy_.message)
      user = CONFIG[bstack111lll1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫಝ")]
      key = CONFIG[bstack111lll1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ಞ")]
      url = bstack111lll1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࢁࡽ࠻ࡽࢀࡄࡦࡶࡩ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠰ࡽࢀ࠲࡯ࡹ࡯࡯ࠩಟ").format(user, key, bstack1llll11_opy_)
      headers = {
        bstack111lll1l1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫಠ"): bstack111lll1l1_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩಡ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack11ll111ll_opy_.format(str(e)))
  if bstack1l1111111_opy_:
    bstack111lll_opy_(bstack1l1111111_opy_)
  if bstack1l111ll11_opy_:
    bstack1l11l1_opy_(bstack1l111ll11_opy_)
  bstack1l1l1_opy_(self, test)
def bstack111ll1ll_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1lll11111_opy_
  bstack1lll11111_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack11lll11_opy_
  bstack11lll11_opy_ = self._test
def bstack11ll1ll1l_opy_():
  global bstack1l1l1l1l1_opy_
  try:
    if os.path.exists(bstack1l1l1l1l1_opy_):
      os.remove(bstack1l1l1l1l1_opy_)
  except Exception as e:
    logger.debug(bstack111lll1l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪಢ") + str(e))
def bstack11ll1111l_opy_():
  global bstack1l1l1l1l1_opy_
  bstack1ll11llll_opy_ = {}
  try:
    if not os.path.isfile(bstack1l1l1l1l1_opy_):
      with open(bstack1l1l1l1l1_opy_, bstack111lll1l1_opy_ (u"ࠨࡹࠪಣ")):
        pass
      with open(bstack1l1l1l1l1_opy_, bstack111lll1l1_opy_ (u"ࠤࡺ࠯ࠧತ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack1l1l1l1l1_opy_):
      bstack1ll11llll_opy_ = json.load(open(bstack1l1l1l1l1_opy_, bstack111lll1l1_opy_ (u"ࠪࡶࡧ࠭ಥ")))
  except Exception as e:
    logger.debug(bstack111lll1l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ದ") + str(e))
  finally:
    return bstack1ll11llll_opy_
def bstack1l1111_opy_(platform_index, item_index):
  global bstack1l1l1l1l1_opy_
  try:
    bstack1ll11llll_opy_ = bstack11ll1111l_opy_()
    bstack1ll11llll_opy_[item_index] = platform_index
    with open(bstack1l1l1l1l1_opy_, bstack111lll1l1_opy_ (u"ࠧࡽࠫࠣಧ")) as outfile:
      json.dump(bstack1ll11llll_opy_, outfile)
  except Exception as e:
    logger.debug(bstack111lll1l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡹࡵ࡭ࡹ࡯࡮ࡨࠢࡷࡳࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫನ") + str(e))
def bstack11llll1ll_opy_(bstack11l11ll1_opy_):
  global CONFIG
  bstack111l11l1_opy_ = bstack111lll1l1_opy_ (u"ࠧࠨ಩")
  if not bstack111lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಪ") in CONFIG:
    logger.info(bstack111lll1l1_opy_ (u"ࠩࡑࡳࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠡࡲࡤࡷࡸ࡫ࡤࠡࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࠦࡲࡦࡲࡲࡶࡹࠦࡦࡰࡴࠣࡖࡴࡨ࡯ࡵࠢࡵࡹࡳ࠭ಫ"))
  try:
    platform = CONFIG[bstack111lll1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಬ")][bstack11l11ll1_opy_]
    if bstack111lll1l1_opy_ (u"ࠫࡴࡹࠧಭ") in platform:
      bstack111l11l1_opy_ += str(platform[bstack111lll1l1_opy_ (u"ࠬࡵࡳࠨಮ")]) + bstack111lll1l1_opy_ (u"࠭ࠬࠡࠩಯ")
    if bstack111lll1l1_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪರ") in platform:
      bstack111l11l1_opy_ += str(platform[bstack111lll1l1_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫಱ")]) + bstack111lll1l1_opy_ (u"ࠩ࠯ࠤࠬಲ")
    if bstack111lll1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧಳ") in platform:
      bstack111l11l1_opy_ += str(platform[bstack111lll1l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ಴")]) + bstack111lll1l1_opy_ (u"ࠬ࠲ࠠࠨವ")
    if bstack111lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨಶ") in platform:
      bstack111l11l1_opy_ += str(platform[bstack111lll1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩಷ")]) + bstack111lll1l1_opy_ (u"ࠨ࠮ࠣࠫಸ")
    if bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧಹ") in platform:
      bstack111l11l1_opy_ += str(platform[bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ಺")]) + bstack111lll1l1_opy_ (u"ࠫ࠱ࠦࠧ಻")
    if bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ಼࠭") in platform:
      bstack111l11l1_opy_ += str(platform[bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧಽ")]) + bstack111lll1l1_opy_ (u"ࠧ࠭ࠢࠪಾ")
  except Exception as e:
    logger.debug(bstack111lll1l1_opy_ (u"ࠨࡕࡲࡱࡪࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡴࡶࡵ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡷ࡫ࡰࡰࡴࡷࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡵ࡮ࠨಿ") + str(e))
  finally:
    if bstack111l11l1_opy_[len(bstack111l11l1_opy_) - 2:] == bstack111lll1l1_opy_ (u"ࠩ࠯ࠤࠬೀ"):
      bstack111l11l1_opy_ = bstack111l11l1_opy_[:-2]
    return bstack111l11l1_opy_
def bstack1l11ll1ll_opy_(path, bstack111l11l1_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1ll11l1ll_opy_ = ET.parse(path)
    bstack1l1lllll1_opy_ = bstack1ll11l1ll_opy_.getroot()
    bstack1l11l1l11_opy_ = None
    for suite in bstack1l1lllll1_opy_.iter(bstack111lll1l1_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩು")):
      if bstack111lll1l1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫೂ") in suite.attrib:
        suite.attrib[bstack111lll1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪೃ")] += bstack111lll1l1_opy_ (u"࠭ࠠࠨೄ") + bstack111l11l1_opy_
        bstack1l11l1l11_opy_ = suite
    bstack1l11lllll_opy_ = None
    for robot in bstack1l1lllll1_opy_.iter(bstack111lll1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭೅")):
      bstack1l11lllll_opy_ = robot
    bstack11l1111l_opy_ = len(bstack1l11lllll_opy_.findall(bstack111lll1l1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧೆ")))
    if bstack11l1111l_opy_ == 1:
      bstack1l11lllll_opy_.remove(bstack1l11lllll_opy_.findall(bstack111lll1l1_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨೇ"))[0])
      bstack1lllll111_opy_ = ET.Element(bstack111lll1l1_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩೈ"), attrib={bstack111lll1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ೉"):bstack111lll1l1_opy_ (u"࡙ࠬࡵࡪࡶࡨࡷࠬೊ"), bstack111lll1l1_opy_ (u"࠭ࡩࡥࠩೋ"):bstack111lll1l1_opy_ (u"ࠧࡴ࠲ࠪೌ")})
      bstack1l11lllll_opy_.insert(1, bstack1lllll111_opy_)
      bstack1l1lll1l_opy_ = None
      for suite in bstack1l11lllll_opy_.iter(bstack111lll1l1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫್ࠧ")):
        bstack1l1lll1l_opy_ = suite
      bstack1l1lll1l_opy_.append(bstack1l11l1l11_opy_)
      bstack1ll1ll_opy_ = None
      for status in bstack1l11l1l11_opy_.iter(bstack111lll1l1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ೎")):
        bstack1ll1ll_opy_ = status
      bstack1l1lll1l_opy_.append(bstack1ll1ll_opy_)
    bstack1ll11l1ll_opy_.write(path)
  except Exception as e:
    logger.debug(bstack111lll1l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡳࡵ࡬ࡲ࡬ࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠨ೏") + str(e))
def bstack1l11l11l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1llllll1_opy_
  global CONFIG
  if bstack111lll1l1_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣ೐") in options:
    del options[bstack111lll1l1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡵࡧࡴࡩࠤ೑")]
  bstack1ll11_opy_ = bstack11ll1111l_opy_()
  for bstack11l11l1_opy_ in bstack1ll11_opy_.keys():
    path = os.path.join(os.getcwd(), bstack111lll1l1_opy_ (u"࠭ࡰࡢࡤࡲࡸࡤࡸࡥࡴࡷ࡯ࡸࡸ࠭೒"), str(bstack11l11l1_opy_), bstack111lll1l1_opy_ (u"ࠧࡰࡷࡷࡴࡺࡺ࠮ࡹ࡯࡯ࠫ೓"))
    bstack1l11ll1ll_opy_(path, bstack11llll1ll_opy_(bstack1ll11_opy_[bstack11l11l1_opy_]))
  bstack11ll1ll1l_opy_()
  return bstack1llllll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack11lll11l_opy_(self, ff_profile_dir):
  global bstack11l1l1ll_opy_
  if not ff_profile_dir:
    return None
  return bstack11l1l1ll_opy_(self, ff_profile_dir)
def bstack1l11lll1_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack111l1_opy_
  bstack11lll11ll_opy_ = []
  if bstack111lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ೔") in CONFIG:
    bstack11lll11ll_opy_ = CONFIG[bstack111lll1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೕ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack111lll1l1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࠦೖ")],
      pabot_args[bstack111lll1l1_opy_ (u"ࠦࡻ࡫ࡲࡣࡱࡶࡩࠧ೗")],
      argfile,
      pabot_args.get(bstack111lll1l1_opy_ (u"ࠧ࡮ࡩࡷࡧࠥ೘")),
      pabot_args[bstack111lll1l1_opy_ (u"ࠨࡰࡳࡱࡦࡩࡸࡹࡥࡴࠤ೙")],
      platform[0],
      bstack111l1_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack111lll1l1_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡨ࡬ࡰࡪࡹࠢ೚")] or [(bstack111lll1l1_opy_ (u"ࠣࠤ೛"), None)]
    for platform in enumerate(bstack11lll11ll_opy_)
  ]
def bstack1l111llll_opy_(self, datasources, outs_dir, options,
  execution_item, command, verbose, argfile,
  hive=None, processes=0,platform_index=0,bstack1l11l1l1_opy_=bstack111lll1l1_opy_ (u"ࠩࠪ೜")):
  global bstack1l1l111l1_opy_
  self.platform_index = platform_index
  self.bstack1lll1l111_opy_ = bstack1l11l1l1_opy_
  bstack1l1l111l1_opy_(self, datasources, outs_dir, options,
    execution_item, command, verbose, argfile, hive, processes)
def bstack1lll11l11_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l1ll1l_opy_
  global bstack11l1_opy_
  if not bstack111lll1l1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬೝ") in item.options:
    item.options[bstack111lll1l1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ೞ")] = []
  for v in item.options[bstack111lll1l1_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ೟")]:
    if bstack111lll1l1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜ࠬೠ") in v:
      item.options[bstack111lll1l1_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩೡ")].remove(v)
    if bstack111lll1l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡄࡎࡌࡅࡗࡍࡓࠨೢ") in v:
      item.options[bstack111lll1l1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫೣ")].remove(v)
  item.options[bstack111lll1l1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ೤")].insert(0, bstack111lll1l1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚࠽ࡿࢂ࠭೥").format(item.platform_index))
  item.options[bstack111lll1l1_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ೦")].insert(0, bstack111lll1l1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡊࡅࡇࡎࡒࡇࡆࡒࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔ࠽ࡿࢂ࠭೧").format(item.bstack1lll1l111_opy_))
  if bstack11l1_opy_:
    item.options[bstack111lll1l1_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ೨")].insert(0, bstack111lll1l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡄࡎࡌࡅࡗࡍࡓ࠻ࡽࢀࠫ೩").format(bstack11l1_opy_))
  return bstack1l1ll1l_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack11l1lll_opy_(command, item_index):
  global bstack11l1_opy_
  if bstack11l1_opy_:
    command[0] = command[0].replace(bstack111lll1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ೪"), bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧ೫") + str(item_index) + bstack11l1_opy_, 1)
  else:
    command[0] = command[0].replace(bstack111lll1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ೬"), bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡸࡪ࡫ࠡࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠢ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠡࠩ೭") + str(item_index), 1)
def bstack1llll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack111ll_opy_
  bstack11l1lll_opy_(command, item_index)
  return bstack111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack11l1ll1ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack111ll_opy_
  bstack11l1lll_opy_(command, item_index)
  return bstack111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1l111ll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack111ll_opy_
  bstack11l1lll_opy_(command, item_index)
  return bstack111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def bstack1111_opy_(self, runner, quiet=False, capture=True):
  global bstack1ll111l_opy_
  bstack111l11_opy_ = bstack1ll111l_opy_(self, runner, quiet=False, capture=True)
  if self.exception:
    if not hasattr(runner, bstack111lll1l1_opy_ (u"࠭ࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࡡࡤࡶࡷ࠭೮")):
      runner.exception_arr = []
    if not hasattr(runner, bstack111lll1l1_opy_ (u"ࠧࡦࡺࡦࡣࡹࡸࡡࡤࡧࡥࡥࡨࡱ࡟ࡢࡴࡵࠫ೯")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack111l11_opy_
def bstack1l1ll11_opy_(self, name, context, *args):
  global bstack1lll11l1_opy_
  if name in [bstack111lll1l1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠩ೰"), bstack111lll1l1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫೱ")]:
    bstack1lll11l1_opy_(self, name, context, *args)
  if name == bstack111lll1l1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠫೲ"):
    try:
      if(not bstack11111l_opy_):
        bstack11ll11l1l_opy_ = str(self.feature.name)
        bstack11ll11l11_opy_(context, bstack11ll11l1l_opy_)
        context.browser.execute_script(bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩೳ") + json.dumps(bstack11ll11l1l_opy_) + bstack111lll1l1_opy_ (u"ࠬࢃࡽࠨ೴"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack111lll1l1_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭೵").format(str(e)))
  if name == bstack111lll1l1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩ೶"):
    try:
      if not hasattr(self, bstack111lll1l1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪ೷")):
        self.driver_before_scenario = True
      if(not bstack11111l_opy_):
        scenario_name = args[0].name
        feature_name = bstack11ll11l1l_opy_ = str(self.feature.name)
        bstack11ll11l1l_opy_ = feature_name + bstack111lll1l1_opy_ (u"ࠩࠣ࠱ࠥ࠭೸") + scenario_name
        if self.driver_before_scenario:
          bstack11ll11l11_opy_(context, bstack11ll11l1l_opy_)
          context.browser.execute_script(bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨ೹") + json.dumps(bstack11ll11l1l_opy_) + bstack111lll1l1_opy_ (u"ࠫࢂࢃࠧ೺"))
    except Exception as e:
      logger.debug(bstack111lll1l1_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰ࠼ࠣࡿࢂ࠭೻").format(str(e)))
  if name == bstack111lll1l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧ೼"):
    try:
      bstack11111ll_opy_ = args[0].status.name
      if str(bstack11111ll_opy_).lower() == bstack111lll1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ೽"):
        bstack11l1ll111_opy_ = bstack111lll1l1_opy_ (u"ࠨࠩ೾")
        bstack1ll11l1l_opy_ = bstack111lll1l1_opy_ (u"ࠩࠪ೿")
        bstack111ll1ll1_opy_ = bstack111lll1l1_opy_ (u"ࠪࠫഀ")
        try:
          import traceback
          bstack11l1ll111_opy_ = self.exception.__class__.__name__
          bstack1l111l111_opy_ = traceback.format_tb(self.exc_traceback)
          bstack1ll11l1l_opy_ = bstack111lll1l1_opy_ (u"ࠫࠥ࠭ഁ").join(bstack1l111l111_opy_)
          bstack111ll1ll1_opy_ = bstack1l111l111_opy_[-1]
        except Exception as e:
          logger.debug(bstack11l1l111_opy_.format(str(e)))
        bstack11l1ll111_opy_ += bstack111ll1ll1_opy_
        bstack1l1llll1_opy_(context, json.dumps(str(args[0].name) + bstack111lll1l1_opy_ (u"ࠧࠦ࠭ࠡࡈࡤ࡭ࡱ࡫ࡤࠢ࡞ࡱࠦം") + str(bstack1ll11l1l_opy_)), bstack111lll1l1_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧഃ"))
        if self.driver_before_scenario:
          bstack1llll1l11_opy_(context, bstack111lll1l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢഄ"), bstack11l1ll111_opy_)
        context.browser.execute_script(bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭അ") + json.dumps(str(args[0].name) + bstack111lll1l1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣആ") + str(bstack1ll11l1l_opy_)) + bstack111lll1l1_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪഇ"))
        if self.driver_before_scenario:
          context.browser.execute_script(bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡷࡹࡧࡴࡶࡵࠥ࠾ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ࠲ࠠࠣࡴࡨࡥࡸࡵ࡮ࠣ࠼ࠣࠫഈ") + json.dumps(bstack111lll1l1_opy_ (u"࡙ࠧࡣࡦࡰࡤࡶ࡮ࡵࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤഉ") + str(bstack11l1ll111_opy_)) + bstack111lll1l1_opy_ (u"࠭ࡽࡾࠩഊ"))
      else:
        bstack1l1llll1_opy_(context, bstack111lll1l1_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣഋ"), bstack111lll1l1_opy_ (u"ࠣ࡫ࡱࡪࡴࠨഌ"))
        if self.driver_before_scenario:
          bstack1llll1l11_opy_(context, bstack111lll1l1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ഍"))
        context.browser.execute_script(bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨഎ") + json.dumps(str(args[0].name) + bstack111lll1l1_opy_ (u"ࠦࠥ࠳ࠠࡑࡣࡶࡷࡪࡪࠡࠣഏ")) + bstack111lll1l1_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫഐ"))
        if self.driver_before_scenario:
          context.browser.execute_script(bstack111lll1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡹࡴࡢࡶࡸࡷࠧࡀࠢࡱࡣࡶࡷࡪࡪࠢࡾࡿࠪ഑"))
    except Exception as e:
      logger.debug(bstack111lll1l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩഒ").format(str(e)))
  if name == bstack111lll1l1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨഓ"):
    try:
      if context.failed is True:
        bstack1l1l111ll_opy_ = []
        bstack1l1l11_opy_ = []
        bstack1ll1llll1_opy_ = []
        bstack11llll_opy_ = bstack111lll1l1_opy_ (u"ࠩࠪഔ")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack1l1l111ll_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack1l111l111_opy_ = traceback.format_tb(exc_tb)
            bstack1ll1ll1l_opy_ = bstack111lll1l1_opy_ (u"ࠪࠤࠬക").join(bstack1l111l111_opy_)
            bstack1l1l11_opy_.append(bstack1ll1ll1l_opy_)
            bstack1ll1llll1_opy_.append(bstack1l111l111_opy_[-1])
        except Exception as e:
          logger.debug(bstack11l1l111_opy_.format(str(e)))
        bstack11l1ll111_opy_ = bstack111lll1l1_opy_ (u"ࠫࠬഖ")
        for i in range(len(bstack1l1l111ll_opy_)):
          bstack11l1ll111_opy_ += bstack1l1l111ll_opy_[i] + bstack1ll1llll1_opy_[i] + bstack111lll1l1_opy_ (u"ࠬࡢ࡮ࠨഗ")
        bstack11llll_opy_ = bstack111lll1l1_opy_ (u"࠭ࠠࠨഘ").join(bstack1l1l11_opy_)
        if not self.driver_before_scenario:
          bstack1l1llll1_opy_(context, bstack11llll_opy_, bstack111lll1l1_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨങ"))
          bstack1llll1l11_opy_(context, bstack111lll1l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣച"), bstack11l1ll111_opy_)
          context.browser.execute_script(bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧഛ") + json.dumps(bstack11llll_opy_) + bstack111lll1l1_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪജ"))
          context.browser.execute_script(bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡷࡹࡧࡴࡶࡵࠥ࠾ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ࠲ࠠࠣࡴࡨࡥࡸࡵ࡮ࠣ࠼ࠣࠫഝ") + json.dumps(bstack111lll1l1_opy_ (u"࡙ࠧ࡯࡮ࡧࠣࡷࡨ࡫࡮ࡢࡴ࡬ࡳࡸࠦࡦࡢ࡫࡯ࡩࡩࡀࠠ࡝ࡰࠥഞ") + str(bstack11l1ll111_opy_)) + bstack111lll1l1_opy_ (u"࠭ࡽࡾࠩട"))
      else:
        if not self.driver_before_scenario:
          bstack1l1llll1_opy_(context, bstack111lll1l1_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥ࠻ࠢࠥഠ") + str(self.feature.name) + bstack111lll1l1_opy_ (u"ࠣࠢࡳࡥࡸࡹࡥࡥࠣࠥഡ"), bstack111lll1l1_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢഢ"))
          bstack1llll1l11_opy_(context, bstack111lll1l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥണ"))
          context.browser.execute_script(bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩത") + json.dumps(bstack111lll1l1_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣഥ") + str(self.feature.name) + bstack111lll1l1_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣദ")) + bstack111lll1l1_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭ധ"))
          context.browser.execute_script(bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠤࡳࡥࡸࡹࡥࡥࠤࢀࢁࠬന"))
    except Exception as e:
      logger.debug(bstack111lll1l1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫഩ").format(str(e)))
  if name in [bstack111lll1l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪപ"), bstack111lll1l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬഫ")]:
    bstack1lll11l1_opy_(self, name, context, *args)
    if (name == bstack111lll1l1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ബ") and self.driver_before_scenario) or (name == bstack111lll1l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ഭ") and not self.driver_before_scenario):
      try:
        context.browser.quit()
      except Exception:
        pass
def bstack1lllll1l1_opy_(config, startdir):
  return bstack111lll1l1_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧമ").format(bstack111lll1l1_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢയ"))
class Notset:
  def __repr__(self):
    return bstack111lll1l1_opy_ (u"ࠤ࠿ࡒࡔ࡚ࡓࡆࡖࡁࠦര")
notset = Notset()
def bstack1llllll11_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1111l11l_opy_
  if str(name).lower() == bstack111lll1l1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪറ"):
    return bstack111lll1l1_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥല")
  else:
    return bstack1111l11l_opy_(self, name, default, skip)
def bstack1l1lllll_opy_(item, when):
  global bstack1l1l1ll_opy_
  try:
    bstack1l1l1ll_opy_(item, when)
  except Exception as e:
    pass
def bstack11lll11l1_opy_():
  return
def bstack1l1111ll1_opy_(type, name, status, reason, bstackl_opy_, bstack11l1111ll_opy_):
  bstack1l11111_opy_ = {
    bstack111lll1l1_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬള"): type,
    bstack111lll1l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩഴ"): {}
  }
  if type == bstack111lll1l1_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩവ"):
    bstack1l11111_opy_[bstack111lll1l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫശ")][bstack111lll1l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨഷ")] = bstackl_opy_
    bstack1l11111_opy_[bstack111lll1l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭സ")][bstack111lll1l1_opy_ (u"ࠫࡩࡧࡴࡢࠩഹ")] = json.dumps(str(bstack11l1111ll_opy_))
  if type == bstack111lll1l1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ഺ"):
    bstack1l11111_opy_[bstack111lll1l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴ഻ࠩ")][bstack111lll1l1_opy_ (u"ࠧ࡯ࡣࡰࡩ഼ࠬ")] = name
  if type == bstack111lll1l1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫഽ"):
    bstack1l11111_opy_[bstack111lll1l1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬാ")][bstack111lll1l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪി")] = status
    if status == bstack111lll1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫീ"):
      bstack1l11111_opy_[bstack111lll1l1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨു")][bstack111lll1l1_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ൂ")] = json.dumps(str(reason))
  bstack1lll1111l_opy_ = bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬൃ").format(json.dumps(bstack1l11111_opy_))
  return bstack1lll1111l_opy_
def bstack1ll1111_opy_(item, call, rep):
  global bstack11llll11l_opy_
  global bstack1l111_opy_
  name = bstack111lll1l1_opy_ (u"ࠨࠩൄ")
  try:
    if rep.when == bstack111lll1l1_opy_ (u"ࠩࡦࡥࡱࡲࠧ൅"):
      bstack111111_opy_ = threading.current_thread().name
      bstack11l11lll_opy_ = bstack111111_opy_.split(bstack111lll1l1_opy_ (u"ࠪࡣࡧࡹࡴࡢࡥ࡮ࡣࠬെ"))
      bstack1ll1l1l1l_opy_ = bstack11l11lll_opy_[0]
      bstack1llll11_opy_ = bstack11l11lll_opy_[1]
      threading.current_thread().name = str(bstack1ll1l1l1l_opy_)
      try:
        name = str(rep.nodeid)
        bstack1111l1ll_opy_ = bstack1l1111ll1_opy_(bstack111lll1l1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬേ"), name, bstack111lll1l1_opy_ (u"ࠬ࠭ൈ"), bstack111lll1l1_opy_ (u"࠭ࠧ൉"), bstack111lll1l1_opy_ (u"ࠧࠨൊ"), bstack111lll1l1_opy_ (u"ࠨࠩോ"))
        for driver in bstack1l111_opy_:
          if bstack1llll11_opy_ == driver.session_id:
            driver.execute_script(bstack1111l1ll_opy_)
      except Exception as e:
        logger.debug(bstack111lll1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠩൌ").format(str(e)))
      try:
        status = bstack111lll1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦ്ࠪ") if rep.outcome.lower() == bstack111lll1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫൎ") else bstack111lll1l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ൏")
        reason = bstack111lll1l1_opy_ (u"࠭ࠧ൐")
        if status == bstack111lll1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ൑"):
          reason = rep.longrepr.reprcrash.message
        level = bstack111lll1l1_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭൒") if status == bstack111lll1l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ൓") else bstack111lll1l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩൔ")
        data = name + bstack111lll1l1_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭ൕ") if status == bstack111lll1l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬൖ") else name + bstack111lll1l1_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠡࠡࠩൗ") + reason
        bstack1lll1l11_opy_ = bstack1l1111ll1_opy_(bstack111lll1l1_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩ൘"), bstack111lll1l1_opy_ (u"ࠨࠩ൙"), bstack111lll1l1_opy_ (u"ࠩࠪ൚"), bstack111lll1l1_opy_ (u"ࠪࠫ൛"), level, data)
        bstack1111l1ll_opy_ = bstack1l1111ll1_opy_(bstack111lll1l1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ൜"), bstack111lll1l1_opy_ (u"ࠬ࠭൝"), status, reason, bstack111lll1l1_opy_ (u"࠭ࠧ൞"), bstack111lll1l1_opy_ (u"ࠧࠨൟ"))
        for driver in bstack1l111_opy_:
          if bstack1llll11_opy_ == driver.session_id:
            driver.execute_script(bstack1lll1l11_opy_)
            driver.execute_script(bstack1111l1ll_opy_)
      except Exception as e:
        logger.debug(bstack111lll1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬൠ").format(str(e)))
  except Exception as e:
    logger.debug(bstack111lll1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭ൡ").format(str(e)))
  bstack11llll11l_opy_(item, call, rep)
def bstack1ll1l11_opy_(framework_name):
  global bstack1l1l1ll1_opy_
  global bstack1l111ll_opy_
  bstack1l1l1ll1_opy_ = framework_name
  logger.info(bstack1l1ll1111_opy_.format(bstack1l1l1ll1_opy_.split(bstack111lll1l1_opy_ (u"ࠪ࠱ࠬൢ"))[0]))
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    Service.start = bstack11l111l1l_opy_
    Service.stop = bstack11l11ll11_opy_
    webdriver.Remote.__init__ = bstack1l1lll111_opy_
    webdriver.Remote.get = bstack1lllll11l_opy_
    WebDriver.close = bstack1ll111111_opy_
    bstack1l111ll_opy_ = True
  except Exception as e:
    pass
  bstack1l11ll_opy_()
  if not bstack1l111ll_opy_:
    bstack1ll111l11_opy_(bstack111lll1l1_opy_ (u"ࠦࡕࡧࡣ࡬ࡣࡪࡩࡸࠦ࡮ࡰࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠨൣ"), bstack1ll1l111_opy_)
  if bstack11l111_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack111lll11l_opy_
    except Exception as e:
      logger.error(bstack1l11ll11l_opy_.format(str(e)))
  if (bstack111lll1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ൤") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack11lll11l_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1ll1l1ll1_opy_
      except Exception as e:
        logger.warn(bstack1l1llllll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack11lllllll_opy_
      except Exception as e:
        logger.debug(bstack111ll1lll_opy_ + str(e))
    except Exception as e:
      bstack1ll111l11_opy_(e, bstack1l1llllll_opy_)
    Output.end_test = bstack11l1ll1l1_opy_
    TestStatus.__init__ = bstack111ll1ll_opy_
    QueueItem.__init__ = bstack1l111llll_opy_
    pabot._create_items = bstack1l11lll1_opy_
    try:
      from pabot import __version__ as bstack11llll11_opy_
      if version.parse(bstack11llll11_opy_) >= version.parse(bstack111lll1l1_opy_ (u"࠭࠲࠯࠳࠸࠲࠵࠭൥")):
        pabot._run = bstack1l111ll1_opy_
      elif version.parse(bstack11llll11_opy_) >= version.parse(bstack111lll1l1_opy_ (u"ࠧ࠳࠰࠴࠷࠳࠶ࠧ൦")):
        pabot._run = bstack11l1ll1ll_opy_
      else:
        pabot._run = bstack1llll_opy_
    except Exception as e:
      pabot._run = bstack1llll_opy_
    pabot._create_command_for_execution = bstack1lll11l11_opy_
    pabot._report_results = bstack1l11l11l_opy_
  if bstack111lll1l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ൧") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll111l11_opy_(e, bstack11l1l11_opy_)
    Runner.run_hook = bstack1l1ll11_opy_
    Step.run = bstack1111_opy_
  if bstack111lll1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ൨") in str(framework_name).lower():
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      from _pytest import runner
      pytest_selenium.pytest_report_header = bstack1lllll1l1_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack11lll11l1_opy_
      Config.getoption = bstack1llllll11_opy_
      runner._update_current_test_var = bstack1l1lllll_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1ll1111_opy_
    except Exception as e:
      pass
def bstack1l1l11l_opy_():
  global CONFIG
  if bstack111lll1l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ൩") in CONFIG and int(CONFIG[bstack111lll1l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ൪")]) > 1:
    logger.warn(bstack1ll11l111_opy_)
def bstack11111l1_opy_(arg):
  arg.append(bstack111lll1l1_opy_ (u"ࠧ࠳࠭ࡤࡣࡳࡸࡺࡸࡥ࠾ࡵࡼࡷࠧ൫"))
  arg.append(bstack111lll1l1_opy_ (u"ࠨ࠭ࡘࠤ൬"))
  arg.append(bstack111lll1l1_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫࠺ࡎࡱࡧࡹࡱ࡫ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡ࡫ࡰࡴࡴࡸࡴࡦࡦ࠽ࡴࡾࡺࡥࡴࡶ࠱ࡔࡾࡺࡥࡴࡶ࡚ࡥࡷࡴࡩ࡯ࡩࠥ൭"))
  global CONFIG
  bstack1ll1l11_opy_(bstack1l1l11l1_opy_)
  os.environ[bstack111lll1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩ൮")] = CONFIG[bstack111lll1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ൯")]
  os.environ[bstack111lll1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭൰")] = CONFIG[bstack111lll1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ൱")]
  from _pytest.config import main as bstack11ll1l1_opy_
  bstack11ll1l1_opy_(arg)
def bstack111111ll_opy_(arg):
  bstack1ll1l11_opy_(bstack11l111ll_opy_)
  from behave.__main__ import main as bstack1ll11l1l1_opy_
  bstack1ll11l1l1_opy_(arg)
def bstack11l1ll11_opy_():
  logger.info(bstack11l11l11l_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack111lll1l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ൲"), help=bstack111lll1l1_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡤࡱࡱࡪ࡮࡭ࠧ൳"))
  parser.add_argument(bstack111lll1l1_opy_ (u"ࠧ࠮ࡷࠪ൴"), bstack111lll1l1_opy_ (u"ࠨ࠯࠰ࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬ൵"), help=bstack111lll1l1_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡵࡴࡧࡵࡲࡦࡳࡥࠨ൶"))
  parser.add_argument(bstack111lll1l1_opy_ (u"ࠪ࠱ࡰ࠭൷"), bstack111lll1l1_opy_ (u"ࠫ࠲࠳࡫ࡦࡻࠪ൸"), help=bstack111lll1l1_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾ࠭൹"))
  parser.add_argument(bstack111lll1l1_opy_ (u"࠭࠭ࡧࠩൺ"), bstack111lll1l1_opy_ (u"ࠧ࠮࠯ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬൻ"), help=bstack111lll1l1_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧർ"))
  bstack1111111l_opy_ = parser.parse_args()
  try:
    bstack11llll111_opy_ = bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡩࡨࡲࡪࡸࡩࡤ࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭ൽ")
    if bstack1111111l_opy_.framework and bstack1111111l_opy_.framework not in (bstack111lll1l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪൾ"), bstack111lll1l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬൿ")):
      bstack11llll111_opy_ = bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࡺ࡯࡯࠲ࡸࡧ࡭ࡱ࡮ࡨࠫ඀")
    bstack11l1llll1_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11llll111_opy_)
    bstack11ll1ll_opy_ = open(bstack11l1llll1_opy_, bstack111lll1l1_opy_ (u"࠭ࡲࠨඁ"))
    bstack1lll1111_opy_ = bstack11ll1ll_opy_.read()
    bstack11ll1ll_opy_.close()
    if bstack1111111l_opy_.username:
      bstack1lll1111_opy_ = bstack1lll1111_opy_.replace(bstack111lll1l1_opy_ (u"࡚ࠧࡑࡘࡖࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧං"), bstack1111111l_opy_.username)
    if bstack1111111l_opy_.key:
      bstack1lll1111_opy_ = bstack1lll1111_opy_.replace(bstack111lll1l1_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪඃ"), bstack1111111l_opy_.key)
    if bstack1111111l_opy_.framework:
      bstack1lll1111_opy_ = bstack1lll1111_opy_.replace(bstack111lll1l1_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ඄"), bstack1111111l_opy_.framework)
    file_name = bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭අ")
    file_path = os.path.abspath(file_name)
    bstack1ll1llll_opy_ = open(file_path, bstack111lll1l1_opy_ (u"ࠫࡼ࠭ආ"))
    bstack1ll1llll_opy_.write(bstack1lll1111_opy_)
    bstack1ll1llll_opy_.close()
    logger.info(bstack1ll11lll_opy_)
    try:
      os.environ[bstack111lll1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧඇ")] = bstack1111111l_opy_.framework if bstack1111111l_opy_.framework != None else bstack111lll1l1_opy_ (u"ࠨࠢඈ")
      config = yaml.safe_load(bstack1lll1111_opy_)
      config[bstack111lll1l1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧඉ")] = bstack111lll1l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠮ࡵࡨࡸࡺࡶࠧඊ")
      bstack1ll1lll_opy_(bstack1ll1l1111_opy_, config)
    except Exception as e:
      logger.debug(bstack1l11l11_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1ll111ll_opy_.format(str(e)))
def bstack1ll1lll_opy_(bstack11l1l1111_opy_, config, bstack1111ll11_opy_ = {}):
  global bstack11l111ll1_opy_
  if not config:
    return
  bstack1lll_opy_ = bstack11ll1ll1_opy_ if not bstack11l111ll1_opy_ else ( bstack1ll11ll11_opy_ if bstack111lll1l1_opy_ (u"ࠩࡤࡴࡵ࠭උ") in config else bstack1l1l_opy_ )
  data = {
    bstack111lll1l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬඌ"): config[bstack111lll1l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ඍ")],
    bstack111lll1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨඎ"): config[bstack111lll1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩඏ")],
    bstack111lll1l1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫඐ"): bstack11l1l1111_opy_,
    bstack111lll1l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫඑ"): {
      bstack111lll1l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧඒ"): str(config[bstack111lll1l1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪඓ")]) if bstack111lll1l1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫඔ") in config else bstack111lll1l1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨඕ"),
      bstack111lll1l1_opy_ (u"࠭ࡲࡦࡨࡨࡶࡷ࡫ࡲࠨඖ"): bstack1l11ll1_opy_(os.getenv(bstack111lll1l1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠤ඗"), bstack111lll1l1_opy_ (u"ࠣࠤ඘"))),
      bstack111lll1l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ඙"): bstack111lll1l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪක"),
      bstack111lll1l1_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬඛ"): bstack1lll_opy_,
      bstack111lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨග"): config[bstack111lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩඝ")]if config[bstack111lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪඞ")] else bstack111lll1l1_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤඟ"),
      bstack111lll1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫච"): str(config[bstack111lll1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬඡ")]) if bstack111lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ජ") in config else bstack111lll1l1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨඣ"),
      bstack111lll1l1_opy_ (u"࠭࡯ࡴࠩඤ"): sys.platform,
      bstack111lll1l1_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩඥ"): socket.gethostname()
    }
  }
  update(data[bstack111lll1l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫඦ")], bstack1111ll11_opy_)
  try:
    response = bstack1ll1ll1l1_opy_(bstack111lll1l1_opy_ (u"ࠩࡓࡓࡘ࡚ࠧට"), bstack11l1ll1_opy_, data, config)
    if response:
      logger.debug(bstack1l111ll1l_opy_.format(bstack11l1l1111_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11ll11ll_opy_.format(str(e)))
def bstack1ll1ll1l1_opy_(type, url, data, config):
  bstack1l111l1_opy_ = bstack11l1lll1_opy_.format(url)
  proxies = bstack1ll11ll1_opy_(config, bstack1l111l1_opy_)
  if type == bstack111lll1l1_opy_ (u"ࠪࡔࡔ࡙ࡔࠨඨ"):
    response = requests.post(bstack1l111l1_opy_, json=data,
                    headers={bstack111lll1l1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪඩ"): bstack111lll1l1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨඪ")}, auth=(config[bstack111lll1l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨණ")], config[bstack111lll1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪඬ")]), proxies=proxies)
  return response
def bstack1l11ll1_opy_(framework):
  return bstack111lll1l1_opy_ (u"ࠣࡽࢀ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧත").format(str(framework), __version__) if framework else bstack111lll1l1_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࡼࡿࠥථ").format(__version__)
def bstack1lll11lll_opy_():
  global CONFIG
  if bool(CONFIG):
    return
  try:
    bstack1lll11ll_opy_()
    logger.debug(bstack1111l_opy_.format(str(CONFIG)))
    bstack1lll1llll_opy_()
    bstack1lllllll_opy_()
  except Exception as e:
    logger.error(bstack111lll1l1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴ࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࠢද") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11l11111_opy_
  atexit.register(bstack11l1lllll_opy_)
  signal.signal(signal.SIGINT, bstack11ll1l11l_opy_)
  signal.signal(signal.SIGTERM, bstack11ll1l11l_opy_)
def bstack11l11111_opy_(exctype, value, traceback):
  global bstack1l111_opy_
  try:
    for driver in bstack1l111_opy_:
      driver.execute_script(
        bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡷࡹࡧࡴࡶࡵࠥ࠾ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ࠲ࠠࠣࡴࡨࡥࡸࡵ࡮ࠣ࠼ࠣࠫධ") + json.dumps(bstack111lll1l1_opy_ (u"࡙ࠧࡥࡴࡵ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣන") + str(value)) + bstack111lll1l1_opy_ (u"࠭ࡽࡾࠩ඲"))
  except Exception:
    pass
  bstack1l11ll11_opy_(value)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l11ll11_opy_(message = bstack111lll1l1_opy_ (u"ࠧࠨඳ")):
  global CONFIG
  try:
    if message:
      bstack1111ll11_opy_ = {
        bstack111lll1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧප"): str(message)
      }
      bstack1ll1lll_opy_(bstack111l1l11_opy_, CONFIG, bstack1111ll11_opy_)
    else:
      bstack1ll1lll_opy_(bstack111l1l11_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1l11l11ll_opy_.format(str(e)))
def bstack1111ll1_opy_(bstack1l11111l_opy_, size):
  bstack1l1llll_opy_ = []
  while len(bstack1l11111l_opy_) > size:
    bstack111l11ll_opy_ = bstack1l11111l_opy_[:size]
    bstack1l1llll_opy_.append(bstack111l11ll_opy_)
    bstack1l11111l_opy_   = bstack1l11111l_opy_[size:]
  bstack1l1llll_opy_.append(bstack1l11111l_opy_)
  return bstack1l1llll_opy_
def run_on_browserstack(bstack111l1lll1_opy_=None, bstack111lll111_opy_=None):
  global CONFIG
  global bstack111llll1_opy_
  global bstack11l111l_opy_
  bstack1111111_opy_ = bstack111lll1l1_opy_ (u"ࠩࠪඵ")
  if bstack111l1lll1_opy_:
    CONFIG = bstack111l1lll1_opy_[bstack111lll1l1_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪබ")]
    bstack111llll1_opy_ = bstack111l1lll1_opy_[bstack111lll1l1_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬභ")]
    bstack11l111l_opy_ = bstack111l1lll1_opy_[bstack111lll1l1_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧම")]
    bstack1111111_opy_ = bstack111lll1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ඹ")
  if len(sys.argv) <= 1:
    logger.critical(bstack1llll1lll_opy_)
    return
  if sys.argv[1] == bstack111lll1l1_opy_ (u"ࠧ࠮࠯ࡹࡩࡷࡹࡩࡰࡰࠪය")  or sys.argv[1] == bstack111lll1l1_opy_ (u"ࠨ࠯ࡹࠫර"):
    logger.info(bstack111lll1l1_opy_ (u"ࠩࡅࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡒࡼࡸ࡭ࡵ࡮ࠡࡕࡇࡏࠥࡼࡻࡾࠩ඼").format(__version__))
    return
  if sys.argv[1] == bstack111lll1l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩල"):
    bstack11l1ll11_opy_()
    return
  args = sys.argv
  bstack1lll11lll_opy_()
  global bstack1lll111ll_opy_
  global bstack11ll11lll_opy_
  global bstack111lll1_opy_
  global bstack111l_opy_
  global bstack111l1_opy_
  global bstack11l1_opy_
  global bstack1l1ll111_opy_
  if not bstack1111111_opy_:
    if args[1] == bstack111lll1l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ඾") or args[1] == bstack111lll1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭඿"):
      bstack1111111_opy_ = bstack111lll1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ව")
      args = args[2:]
    elif args[1] == bstack111lll1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ශ"):
      bstack1111111_opy_ = bstack111lll1l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧෂ")
      args = args[2:]
    elif args[1] == bstack111lll1l1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨස"):
      bstack1111111_opy_ = bstack111lll1l1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩහ")
      args = args[2:]
    elif args[1] == bstack111lll1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬළ"):
      bstack1111111_opy_ = bstack111lll1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ෆ")
      args = args[2:]
    elif args[1] == bstack111lll1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭෇"):
      bstack1111111_opy_ = bstack111lll1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ෈")
      args = args[2:]
    elif args[1] == bstack111lll1l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ෉"):
      bstack1111111_opy_ = bstack111lll1l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦ්ࠩ")
      args = args[2:]
    else:
      if not bstack111lll1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭෋") in CONFIG or str(CONFIG[bstack111lll1l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ෌")]).lower() in [bstack111lll1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ෍"), bstack111lll1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧ෎")]:
        bstack1111111_opy_ = bstack111lll1l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧා")
        args = args[1:]
      elif str(CONFIG[bstack111lll1l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫැ")]).lower() == bstack111lll1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨෑ"):
        bstack1111111_opy_ = bstack111lll1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩි")
        args = args[1:]
      elif str(CONFIG[bstack111lll1l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧී")]).lower() == bstack111lll1l1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫු"):
        bstack1111111_opy_ = bstack111lll1l1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ෕")
        args = args[1:]
      elif str(CONFIG[bstack111lll1l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪූ")]).lower() == bstack111lll1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ෗"):
        bstack1111111_opy_ = bstack111lll1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩෘ")
        args = args[1:]
      elif str(CONFIG[bstack111lll1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ෙ")]).lower() == bstack111lll1l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫේ"):
        bstack1111111_opy_ = bstack111lll1l1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬෛ")
        args = args[1:]
      else:
        os.environ[bstack111lll1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨො")] = bstack1111111_opy_
        bstack11l_opy_(bstack1llll1l1_opy_)
  global bstack1l11l111_opy_
  if bstack111l1lll1_opy_:
    try:
      os.environ[bstack111lll1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩෝ")] = bstack1111111_opy_
      bstack1ll1lll_opy_(bstack11lll1_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack1l11l11ll_opy_.format(str(e)))
  global bstack1l1_opy_
  global bstack1l1l1_opy_
  global bstack1l11l1_opy_
  global bstack111lll_opy_
  global bstack1lll11111_opy_
  global bstack11l1l1ll_opy_
  global bstack111ll_opy_
  global bstack1l1l111l1_opy_
  global bstack1l1ll1l_opy_
  global bstack11l1l_opy_
  global bstack1lll11l1_opy_
  global bstack1ll111l_opy_
  global bstack1ll1l11l_opy_
  global bstack11111_opy_
  global bstack1111l11l_opy_
  global bstack1l1l1ll_opy_
  global bstack1llllll1_opy_
  global bstack11llll11l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l1_opy_ = webdriver.Remote.__init__
    bstack11l1l_opy_ = WebDriver.close
    bstack1ll1l11l_opy_ = WebDriver.get
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1l11l111_opy_ = Popen.__init__
  except Exception as e:
    pass
  if bstack11lll1l11_opy_():
    if bstack1l1llll1l_opy_() < version.parse(bstack11l1l1ll1_opy_):
      logger.error(bstack1l1ll1ll1_opy_.format(bstack1l1llll1l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack11111_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1l11ll11l_opy_.format(str(e)))
  if bstack1111111_opy_ != bstack111lll1l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨෞ") or (bstack1111111_opy_ == bstack111lll1l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩෟ") and not bstack111l1lll1_opy_):
    bstack1lll11ll1_opy_()
  if (bstack1111111_opy_ in [bstack111lll1l1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ෠"), bstack111lll1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ෡"), bstack111lll1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭෢")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack11lll11l_opy_
        bstack111lll_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1l1llllll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1l11l1_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack111ll1lll_opy_ + str(e))
    except Exception as e:
      bstack1ll111l11_opy_(e, bstack1l1llllll_opy_)
    if bstack1111111_opy_ != bstack111lll1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ෣"):
      bstack11ll1ll1l_opy_()
    bstack1l1l1_opy_ = Output.end_test
    bstack1lll11111_opy_ = TestStatus.__init__
    bstack111ll_opy_ = pabot._run
    bstack1l1l111l1_opy_ = QueueItem.__init__
    bstack1l1ll1l_opy_ = pabot._create_command_for_execution
    bstack1llllll1_opy_ = pabot._report_results
  if bstack1111111_opy_ == bstack111lll1l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ෤"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll111l11_opy_(e, bstack11l1l11_opy_)
    bstack1lll11l1_opy_ = Runner.run_hook
    bstack1ll111l_opy_ = Step.run
  if bstack1111111_opy_ == bstack111lll1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ෥"):
    try:
      from _pytest.config import Config
      bstack1111l11l_opy_ = Config.getoption
      from _pytest import runner
      bstack1l1l1ll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1l11l1l1l_opy_)
    try:
      from pytest_bdd import reporting
      bstack11llll11l_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack111lll1l1_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪ෦"))
  if bstack1111111_opy_ == bstack111lll1l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ෧"):
    bstack11ll11lll_opy_ = True
    if bstack111l1lll1_opy_:
      bstack111l1_opy_ = CONFIG.get(bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ෨"), {}).get(bstack111lll1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ෩"))
      bstack1ll1l11_opy_(bstack11ll1l1ll_opy_)
      sys.path.append(os.path.dirname(os.path.abspath(bstack111l1lll1_opy_[bstack111lll1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ෪")])))
      mod_globals = globals()
      mod_globals[bstack111lll1l1_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩ෫")] = bstack111lll1l1_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪ෬")
      mod_globals[bstack111lll1l1_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫ෭")] = os.path.abspath(bstack111l1lll1_opy_[bstack111lll1l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭෮")])
      global bstack1l111_opy_
      try:
        exec(open(bstack111l1lll1_opy_[bstack111lll1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ෯")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack111lll1l1_opy_ (u"ࠬࡉࡡࡶࡩ࡫ࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠬ෰").format(str(e)))
          for driver in bstack1l111_opy_:
            bstack111lll111_opy_.append({
              bstack111lll1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ෱"): bstack111l1lll1_opy_[bstack111lll1l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪෲ")],
              bstack111lll1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧෳ"): str(e),
              bstack111lll1l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ෴"): multiprocessing.current_process().name
            })
            driver.execute_script(
              bstack111lll1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡶࡸࡦࡺࡵࡴࠤ࠽ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ࠱ࠦࠢࡳࡧࡤࡷࡴࡴࠢ࠻ࠢࠪ෵") + json.dumps(bstack111lll1l1_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢ෶") + str(e)) + bstack111lll1l1_opy_ (u"ࠬࢃࡽࠨ෷"))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l111_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      bstack11l11ll1l_opy_()
      bstack1l1l11l_opy_()
      if bstack111lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ෸") in CONFIG:
        bstack1ll1lll1l_opy_ = {
          bstack111lll1l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ෹"): args[0],
          bstack111lll1l1_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨ෺"): CONFIG,
          bstack111lll1l1_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪ෻"): bstack111llll1_opy_,
          bstack111lll1l1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ෼"): bstack11l111l_opy_
        }
        bstack111ll111l_opy_ = []
        manager = multiprocessing.Manager()
        bstack11ll1l11_opy_ = manager.list()
        for index, platform in enumerate(CONFIG[bstack111lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ෽")]):
          bstack1ll1lll1l_opy_[bstack111lll1l1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ෾")] = index
          bstack111ll111l_opy_.append(multiprocessing.Process(name=str(index),
                                        target=run_on_browserstack, args=(bstack1ll1lll1l_opy_, bstack11ll1l11_opy_)))
        for t in bstack111ll111l_opy_:
          t.start()
        for t in bstack111ll111l_opy_:
          t.join()
        bstack1l1ll111_opy_ = list(bstack11ll1l11_opy_)
      else:
        bstack1ll1l11_opy_(bstack11ll1l1ll_opy_)
        sys.path.append(os.path.dirname(os.path.abspath(args[0])))
        mod_globals = globals()
        mod_globals[bstack111lll1l1_opy_ (u"࠭࡟ࡠࡰࡤࡱࡪࡥ࡟ࠨ෿")] = bstack111lll1l1_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩ฀")
        mod_globals[bstack111lll1l1_opy_ (u"ࠨࡡࡢࡪ࡮ࡲࡥࡠࡡࠪก")] = os.path.abspath(args[0])
        exec(open(args[0]).read(), mod_globals)
  elif bstack1111111_opy_ == bstack111lll1l1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨข") or bstack1111111_opy_ == bstack111lll1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩฃ"):
    try:
      from pabot import pabot
    except Exception as e:
      bstack1ll111l11_opy_(e, bstack1l1llllll_opy_)
    bstack11l11ll1l_opy_()
    bstack1ll1l11_opy_(bstack111lllll_opy_)
    if bstack111lll1l1_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩค") in args:
      i = args.index(bstack111lll1l1_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪฅ"))
      args.pop(i)
      args.pop(i)
    args.insert(0, str(bstack1lll111ll_opy_))
    args.insert(0, str(bstack111lll1l1_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫฆ")))
    pabot.main(args)
  elif bstack1111111_opy_ == bstack111lll1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨง"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1ll111l11_opy_(e, bstack1l1llllll_opy_)
    for a in args:
      if bstack111lll1l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞ࠧจ") in a:
        bstack111l_opy_ = int(a.split(bstack111lll1l1_opy_ (u"ࠩ࠽ࠫฉ"))[1])
      if bstack111lll1l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧช") in a:
        bstack111l1_opy_ = str(a.split(bstack111lll1l1_opy_ (u"ࠫ࠿࠭ซ"))[1])
      if bstack111lll1l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬฌ") in a:
        bstack11l1_opy_ = str(a.split(bstack111lll1l1_opy_ (u"࠭࠺ࠨญ"))[1])
    bstack1111ll_opy_ = None
    if bstack111lll1l1_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭ฎ") in args:
      i = args.index(bstack111lll1l1_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠧฏ"))
      args.pop(i)
      bstack1111ll_opy_ = args.pop(i)
    if bstack1111ll_opy_ is not None:
      global bstack1llll111l_opy_
      bstack1llll111l_opy_ = bstack1111ll_opy_
    bstack1ll1l11_opy_(bstack111lllll_opy_)
    run_cli(args)
  elif bstack1111111_opy_ == bstack111lll1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩฐ"):
    try:
      from _pytest.config import _prepareconfig
      from _pytest.config import Config
      from _pytest import runner
      import importlib
      bstack11llllll_opy_ = importlib.find_loader(bstack111lll1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬฑ"))
    except Exception as e:
      logger.warn(e, bstack1l11l1l1l_opy_)
    bstack11l11ll1l_opy_()
    try:
      if bstack111lll1l1_opy_ (u"ࠫ࠲࠳ࡤࡳ࡫ࡹࡩࡷ࠭ฒ") in args:
        i = args.index(bstack111lll1l1_opy_ (u"ࠬ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠧณ"))
        args.pop(i+1)
        args.pop(i)
      if bstack111lll1l1_opy_ (u"࠭࠭࠮ࡲ࡯ࡹ࡬࡯࡮ࡴࠩด") in args:
        i = args.index(bstack111lll1l1_opy_ (u"ࠧ࠮࠯ࡳࡰࡺ࡭ࡩ࡯ࡵࠪต"))
        args.pop(i+1)
        args.pop(i)
      if bstack111lll1l1_opy_ (u"ࠨ࠯ࡳࠫถ") in args:
        i = args.index(bstack111lll1l1_opy_ (u"ࠩ࠰ࡴࠬท"))
        args.pop(i+1)
        args.pop(i)
      if bstack111lll1l1_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫธ") in args:
        i = args.index(bstack111lll1l1_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬน"))
        args.pop(i+1)
        args.pop(i)
      if bstack111lll1l1_opy_ (u"ࠬ࠳࡮ࠨบ") in args:
        i = args.index(bstack111lll1l1_opy_ (u"࠭࠭࡯ࠩป"))
        args.pop(i+1)
        args.pop(i)
    except Exception as exc:
      logger.error(str(exc))
    config = _prepareconfig(args)
    bstack1l1111l1l_opy_ = config.args
    bstack11l1ll_opy_ = config.invocation_params.args
    bstack11l1ll_opy_ = list(bstack11l1ll_opy_)
    bstack111l1lll_opy_ = [os.path.normpath(item) for item in bstack1l1111l1l_opy_]
    bstack111111l_opy_ = [os.path.normpath(item) for item in bstack11l1ll_opy_]
    bstack11l1l1l11_opy_ = [item for item in bstack111111l_opy_ if item not in bstack111l1lll_opy_]
    if bstack111lll1l1_opy_ (u"ࠧ࠮࠯ࡦࡥࡨ࡮ࡥ࠮ࡥ࡯ࡩࡦࡸࠧผ") not in bstack11l1l1l11_opy_:
      bstack11l1l1l11_opy_.append(bstack111lll1l1_opy_ (u"ࠨ࠯࠰ࡧࡦࡩࡨࡦ࠯ࡦࡰࡪࡧࡲࠨฝ"))
    import platform as pf
    if pf.system().lower() == bstack111lll1l1_opy_ (u"ࠩࡺ࡭ࡳࡪ࡯ࡸࡵࠪพ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1l1111l1l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1ll11l11l_opy_)))
                    for bstack1ll11l11l_opy_ in bstack1l1111l1l_opy_]
    if (bstack11111l_opy_):
      bstack11l1l1l11_opy_.append(bstack111lll1l1_opy_ (u"ࠪ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧฟ"))
      bstack11l1l1l11_opy_.append(bstack111lll1l1_opy_ (u"࡙ࠫࡸࡵࡦࠩภ"))
    bstack11l1l1l11_opy_.append(bstack111lll1l1_opy_ (u"ࠬ࠳ࡰࠨม"))
    bstack11l1l1l11_opy_.append(bstack111lll1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠫย"))
    bstack11l1l1l11_opy_.append(bstack111lll1l1_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩร"))
    bstack11l1l1l11_opy_.append(bstack111lll1l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨฤ"))
    bstack1l1ll_opy_ = []
    for spec in bstack1l1111l1l_opy_:
      bstack1l1ll1ll_opy_ = []
      bstack1l1ll1ll_opy_.append(spec)
      bstack1l1ll1ll_opy_ += bstack11l1l1l11_opy_
      bstack1l1ll_opy_.append(bstack1l1ll1ll_opy_)
    bstack111lll1_opy_ = True
    bstack1l1l11ll1_opy_ = 1
    if bstack111lll1l1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩล") in CONFIG:
      bstack1l1l11ll1_opy_ = CONFIG[bstack111lll1l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪฦ")]
    bstack111llll1l_opy_ = int(bstack1l1l11ll1_opy_)*int(len(CONFIG[bstack111lll1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧว")]))
    execution_items = []
    for bstack1l1ll1ll_opy_ in bstack1l1ll_opy_:
      for index, _ in enumerate(CONFIG[bstack111lll1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨศ")]):
        item = {}
        item[bstack111lll1l1_opy_ (u"࠭ࡡࡳࡩࠪษ")] = bstack1l1ll1ll_opy_
        item[bstack111lll1l1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ส")] = index
        execution_items.append(item)
    bstack1ll11111_opy_ = bstack1111ll1_opy_(execution_items, bstack111llll1l_opy_)
    for execution_item in bstack1ll11111_opy_:
      bstack111ll111l_opy_ = []
      for item in execution_item:
        bstack111ll111l_opy_.append(bstack1l111111l_opy_(name=str(item[bstack111lll1l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧห")]),
                                            target=bstack11111l1_opy_,
                                            args=(item[bstack111lll1l1_opy_ (u"ࠩࡤࡶ࡬࠭ฬ")],)))
      for t in bstack111ll111l_opy_:
        t.start()
      for t in bstack111ll111l_opy_:
        t.join()
  elif bstack1111111_opy_ == bstack111lll1l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪอ"):
    try:
      from behave.__main__ import main as bstack1ll11l1l1_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1ll111l11_opy_(e, bstack11l1l11_opy_)
    bstack11l11ll1l_opy_()
    bstack111lll1_opy_ = True
    bstack1l1l11ll1_opy_ = 1
    if bstack111lll1l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫฮ") in CONFIG:
      bstack1l1l11ll1_opy_ = CONFIG[bstack111lll1l1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬฯ")]
    bstack111llll1l_opy_ = int(bstack1l1l11ll1_opy_)*int(len(CONFIG[bstack111lll1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩะ")]))
    config = Configuration(args)
    bstack1l1111l1l_opy_ = config.paths
    bstack1l11ll111_opy_ = []
    for arg in args:
      if os.path.normpath(arg) not in bstack1l1111l1l_opy_:
        bstack1l11ll111_opy_.append(arg)
    import platform as pf
    if pf.system().lower() == bstack111lll1l1_opy_ (u"ࠧࡸ࡫ࡱࡨࡴࡽࡳࠨั"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1l1111l1l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1ll11l11l_opy_)))
                    for bstack1ll11l11l_opy_ in bstack1l1111l1l_opy_]
    bstack1l1ll_opy_ = []
    for spec in bstack1l1111l1l_opy_:
      bstack1l1ll1ll_opy_ = []
      bstack1l1ll1ll_opy_ += bstack1l11ll111_opy_
      bstack1l1ll1ll_opy_.append(spec)
      bstack1l1ll_opy_.append(bstack1l1ll1ll_opy_)
    execution_items = []
    for index, _ in enumerate(CONFIG[bstack111lll1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫา")]):
      for bstack1l1ll1ll_opy_ in bstack1l1ll_opy_:
        item = {}
        item[bstack111lll1l1_opy_ (u"ࠩࡤࡶ࡬࠭ำ")] = bstack111lll1l1_opy_ (u"ࠪࠤࠬิ").join(bstack1l1ll1ll_opy_)
        item[bstack111lll1l1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪี")] = index
        execution_items.append(item)
    bstack1ll11111_opy_ = bstack1111ll1_opy_(execution_items, bstack111llll1l_opy_)
    for execution_item in bstack1ll11111_opy_:
      bstack111ll111l_opy_ = []
      for item in execution_item:
        bstack111ll111l_opy_.append(bstack1l111111l_opy_(name=str(item[bstack111lll1l1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫึ")]),
                                            target=bstack111111ll_opy_,
                                            args=(item[bstack111lll1l1_opy_ (u"࠭ࡡࡳࡩࠪื")],)))
      for t in bstack111ll111l_opy_:
        t.start()
      for t in bstack111ll111l_opy_:
        t.join()
  else:
    bstack11l_opy_(bstack1llll1l1_opy_)
  if not bstack111l1lll1_opy_:
    bstack1l1l1llll_opy_()
def bstack1l1l1llll_opy_():
  [bstack1ll1ll11l_opy_, bstack1l1l11l1l_opy_] = bstack11111ll1_opy_()
  if bstack1ll1ll11l_opy_ is not None and bstack1ll1111ll_opy_() != -1:
    sessions = bstack11ll1l111_opy_(bstack1ll1ll11l_opy_)
    bstack1lll1_opy_(sessions, bstack1l1l11l1l_opy_)
def bstack1lllll11_opy_(bstack11lllll1_opy_):
    if bstack11lllll1_opy_:
        return bstack11lllll1_opy_.capitalize()
    else:
        return bstack11lllll1_opy_
def bstack1l1ll1l1_opy_(bstack11llll1_opy_):
    if bstack111lll1l1_opy_ (u"ࠧ࡯ࡣࡰࡩุࠬ") in bstack11llll1_opy_ and bstack11llll1_opy_[bstack111lll1l1_opy_ (u"ࠨࡰࡤࡱࡪู࠭")] != bstack111lll1l1_opy_ (u"ฺࠩࠪ"):
        return bstack11llll1_opy_[bstack111lll1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨ฻")]
    else:
        bstack11l111l11_opy_ = bstack111lll1l1_opy_ (u"ࠦࠧ฼")
        if bstack111lll1l1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ฽") in bstack11llll1_opy_ and bstack11llll1_opy_[bstack111lll1l1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭฾")] != None:
            bstack11l111l11_opy_ += bstack11llll1_opy_[bstack111lll1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ฿")] + bstack111lll1l1_opy_ (u"ࠣ࠮ࠣࠦเ")
            if bstack11llll1_opy_[bstack111lll1l1_opy_ (u"ࠩࡲࡷࠬแ")] == bstack111lll1l1_opy_ (u"ࠥ࡭ࡴࡹࠢโ"):
                bstack11l111l11_opy_ += bstack111lll1l1_opy_ (u"ࠦ࡮ࡕࡓࠡࠤใ")
            bstack11l111l11_opy_ += (bstack11llll1_opy_[bstack111lll1l1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩไ")] or bstack111lll1l1_opy_ (u"࠭ࠧๅ"))
            return bstack11l111l11_opy_
        else:
            bstack11l111l11_opy_ += bstack1lllll11_opy_(bstack11llll1_opy_[bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨๆ")]) + bstack111lll1l1_opy_ (u"ࠣࠢࠥ็") + (bstack11llll1_opy_[bstack111lll1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱ่ࠫ")] or bstack111lll1l1_opy_ (u"้ࠪࠫ")) + bstack111lll1l1_opy_ (u"ࠦ࠱๊ࠦࠢ")
            if bstack11llll1_opy_[bstack111lll1l1_opy_ (u"ࠬࡵࡳࠨ๋")] == bstack111lll1l1_opy_ (u"ࠨࡗࡪࡰࡧࡳࡼࡹࠢ์"):
                bstack11l111l11_opy_ += bstack111lll1l1_opy_ (u"ࠢࡘ࡫ࡱࠤࠧํ")
            bstack11l111l11_opy_ += bstack11llll1_opy_[bstack111lll1l1_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ๎")] or bstack111lll1l1_opy_ (u"ࠩࠪ๏")
            return bstack11l111l11_opy_
def bstack1lll11l_opy_(bstack111l11l_opy_):
    if bstack111l11l_opy_ == bstack111lll1l1_opy_ (u"ࠥࡨࡴࡴࡥࠣ๐"):
        return bstack111lll1l1_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡧࡳࡧࡨࡲࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡧࡳࡧࡨࡲࠧࡄࡃࡰ࡯ࡳࡰࡪࡺࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ๑")
    elif bstack111l11l_opy_ == bstack111lll1l1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ๒"):
        return bstack111lll1l1_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡴࡨࡨࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡲࡦࡦࠥࡂࡋࡧࡩ࡭ࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ๓")
    elif bstack111l11l_opy_ == bstack111lll1l1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ๔"):
        return bstack111lll1l1_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽࡫ࡷ࡫ࡥ࡯࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥ࡫ࡷ࡫ࡥ࡯ࠤࡁࡔࡦࡹࡳࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ๕")
    elif bstack111l11l_opy_ == bstack111lll1l1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ๖"):
        return bstack111lll1l1_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡸࡥࡥ࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡶࡪࡪࠢ࠿ࡇࡵࡶࡴࡸ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ๗")
    elif bstack111l11l_opy_ == bstack111lll1l1_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧ๘"):
        return bstack111lll1l1_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࠤࡧࡨࡥ࠸࠸࠶࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࠦࡩࡪࡧ࠳࠳࠸ࠥࡂ࡙࡯࡭ࡦࡱࡸࡸࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ๙")
    elif bstack111l11l_opy_ == bstack111lll1l1_opy_ (u"ࠨࡲࡶࡰࡱ࡭ࡳ࡭ࠢ๚"):
        return bstack111lll1l1_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࡕࡹࡳࡴࡩ࡯ࡩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ๛")
    else:
        return bstack111lll1l1_opy_ (u"ࠨ࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡧࡲࡡࡤ࡭࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡧࡲࡡࡤ࡭ࠥࡂࠬ๜")+bstack1lllll11_opy_(bstack111l11l_opy_)+bstack111lll1l1_opy_ (u"ࠩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ๝")
def bstack11l1llll_opy_(session):
    return bstack111lll1l1_opy_ (u"ࠪࡀࡹࡸࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡳࡱࡺࠦࡃࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠠࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡰࡤࡱࡪࠨ࠾࠽ࡣࠣ࡬ࡷ࡫ࡦ࠾ࠤࡾࢁࠧࠦࡴࡢࡴࡪࡩࡹࡃࠢࡠࡤ࡯ࡥࡳࡱࠢ࠿ࡽࢀࡀ࠴ࡧ࠾࠽࠱ࡷࡨࡃࢁࡽࡼࡿ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁ࠵ࡴࡳࡀࠪ๞").format(session[bstack111lll1l1_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨ๟")],bstack1l1ll1l1_opy_(session), bstack1lll11l_opy_(session[bstack111lll1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡺࡡࡵࡷࡶࠫ๠")]), bstack1lll11l_opy_(session[bstack111lll1l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭๡")]), bstack1lllll11_opy_(session[bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ๢")] or session[bstack111lll1l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ๣")] or bstack111lll1l1_opy_ (u"ࠩࠪ๤")) + bstack111lll1l1_opy_ (u"ࠥࠤࠧ๥") + (session[bstack111lll1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭๦")] or bstack111lll1l1_opy_ (u"ࠬ࠭๧")), session[bstack111lll1l1_opy_ (u"࠭࡯ࡴࠩ๨")] + bstack111lll1l1_opy_ (u"ࠢࠡࠤ๩") + session[bstack111lll1l1_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ๪")], session[bstack111lll1l1_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ๫")] or bstack111lll1l1_opy_ (u"ࠪࠫ๬"), session[bstack111lll1l1_opy_ (u"ࠫࡨࡸࡥࡢࡶࡨࡨࡤࡧࡴࠨ๭")] if session[bstack111lll1l1_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩ๮")] else bstack111lll1l1_opy_ (u"࠭ࠧ๯"))
def bstack1lll1_opy_(sessions, bstack1l1l11l1l_opy_):
  try:
    bstack1l1lll_opy_ = bstack111lll1l1_opy_ (u"ࠢࠣ๰")
    if not os.path.exists(bstack11ll1ll11_opy_):
      os.mkdir(bstack11ll1ll11_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111lll1l1_opy_ (u"ࠨࡣࡶࡷࡪࡺࡳ࠰ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭๱")), bstack111lll1l1_opy_ (u"ࠩࡵࠫ๲")) as f:
      bstack1l1lll_opy_ = f.read()
    bstack1l1lll_opy_ = bstack1l1lll_opy_.replace(bstack111lll1l1_opy_ (u"ࠪࡿࠪࡘࡅࡔࡗࡏࡘࡘࡥࡃࡐࡗࡑࡘࠪࢃࠧ๳"), str(len(sessions)))
    bstack1l1lll_opy_ = bstack1l1lll_opy_.replace(bstack111lll1l1_opy_ (u"ࠫࢀࠫࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠧࢀࠫ๴"), bstack1l1l11l1l_opy_)
    bstack1l1lll_opy_ = bstack1l1lll_opy_.replace(bstack111lll1l1_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡎࡂࡏࡈࠩࢂ࠭๵"), sessions[0].get(bstack111lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡴࡡ࡮ࡧࠪ๶")) if sessions[0] else bstack111lll1l1_opy_ (u"ࠧࠨ๷"))
    with open(os.path.join(bstack11ll1ll11_opy_, bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡳࡧࡳࡳࡷࡺ࠮ࡩࡶࡰࡰࠬ๸")), bstack111lll1l1_opy_ (u"ࠩࡺࠫ๹")) as stream:
      stream.write(bstack1l1lll_opy_.split(bstack111lll1l1_opy_ (u"ࠪࡿ࡙ࠪࡅࡔࡕࡌࡓࡓ࡙࡟ࡅࡃࡗࡅࠪࢃࠧ๺"))[0])
      for session in sessions:
        stream.write(bstack11l1llll_opy_(session))
      stream.write(bstack1l1lll_opy_.split(bstack111lll1l1_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨ๻"))[1])
    logger.info(bstack111lll1l1_opy_ (u"ࠬࡍࡥ࡯ࡧࡵࡥࡹ࡫ࡤࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡣࡷ࡬ࡰࡩࠦࡡࡳࡶ࡬ࡪࡦࡩࡴࡴࠢࡤࡸࠥࢁࡽࠨ๼").format(bstack11ll1ll11_opy_));
  except Exception as e:
    logger.debug(bstack1l111l1l_opy_.format(str(e)))
def bstack11ll1l111_opy_(bstack1ll1ll11l_opy_):
  global CONFIG
  try:
    host = bstack111lll1l1_opy_ (u"࠭ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥࠩ๽") if bstack111lll1l1_opy_ (u"ࠧࡢࡲࡳࠫ๾") in CONFIG else bstack111lll1l1_opy_ (u"ࠨࡣࡳ࡭ࠬ๿")
    user = CONFIG[bstack111lll1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ຀")]
    key = CONFIG[bstack111lll1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ກ")]
    bstack111ll11ll_opy_ = bstack111lll1l1_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪຂ") if bstack111lll1l1_opy_ (u"ࠬࡧࡰࡱࠩ຃") in CONFIG else bstack111lll1l1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨຄ")
    url = bstack111lll1l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠮࡫ࡵࡲࡲࠬ຅").format(user, key, host, bstack111ll11ll_opy_, bstack1ll1ll11l_opy_)
    headers = {
      bstack111lll1l1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧຆ"): bstack111lll1l1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬງ"),
    }
    proxies = bstack1ll11ll1_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack111lll1l1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨຈ")], response.json()))
  except Exception as e:
    logger.debug(bstack11l1l1_opy_.format(str(e)))
def bstack11111ll1_opy_():
  global CONFIG
  try:
    if bstack111lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧຉ") in CONFIG:
      host = bstack111lll1l1_opy_ (u"ࠬࡧࡰࡪ࠯ࡦࡰࡴࡻࡤࠨຊ") if bstack111lll1l1_opy_ (u"࠭ࡡࡱࡲࠪ຋") in CONFIG else bstack111lll1l1_opy_ (u"ࠧࡢࡲ࡬ࠫຌ")
      user = CONFIG[bstack111lll1l1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪຍ")]
      key = CONFIG[bstack111lll1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬຎ")]
      bstack111ll11ll_opy_ = bstack111lll1l1_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩຏ") if bstack111lll1l1_opy_ (u"ࠫࡦࡶࡰࠨຐ") in CONFIG else bstack111lll1l1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧຑ")
      url = bstack111lll1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡼࡿ࠽ࡿࢂࡆࡻࡾ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠯࡬ࡶࡳࡳ࠭ຒ").format(user, key, host, bstack111ll11ll_opy_)
      headers = {
        bstack111lll1l1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭ຓ"): bstack111lll1l1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫດ"),
      }
      if bstack111lll1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫຕ") in CONFIG:
        params = {bstack111lll1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨຖ"):CONFIG[bstack111lll1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧທ")], bstack111lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨຘ"):CONFIG[bstack111lll1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨນ")]}
      else:
        params = {bstack111lll1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬບ"):CONFIG[bstack111lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫປ")]}
      proxies = bstack1ll11ll1_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack1llllllll_opy_ = response.json()[0][bstack111lll1l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡢࡶ࡫࡯ࡨࠬຜ")]
        if bstack1llllllll_opy_:
          bstack1l1l11l1l_opy_ = bstack1llllllll_opy_[bstack111lll1l1_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧຝ")].split(bstack111lll1l1_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦ࠱ࡧࡻࡩ࡭ࡦࠪພ"))[0] + bstack111lll1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡷ࠴࠭ຟ") + bstack1llllllll_opy_[bstack111lll1l1_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩຠ")]
          logger.info(bstack1l1ll1_opy_.format(bstack1l1l11l1l_opy_))
          bstack11l1l1l_opy_ = CONFIG[bstack111lll1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪມ")]
          if bstack111lll1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪຢ") in CONFIG:
            bstack11l1l1l_opy_ += bstack111lll1l1_opy_ (u"ࠩࠣࠫຣ") + CONFIG[bstack111lll1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ຤")]
          if bstack11l1l1l_opy_!= bstack1llllllll_opy_[bstack111lll1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩລ")]:
            logger.debug(bstack1l1l1lll1_opy_.format(bstack1llllllll_opy_[bstack111lll1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ຦")], bstack11l1l1l_opy_))
          return [bstack1llllllll_opy_[bstack111lll1l1_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩວ")], bstack1l1l11l1l_opy_]
    else:
      logger.warn(bstack111llll_opy_)
  except Exception as e:
    logger.debug(bstack111lllll1_opy_.format(str(e)))
  return [None, None]
def bstack1llllll1l_opy_(url, bstack11ll11l_opy_=False):
  global CONFIG
  global bstack1llll111_opy_
  if not bstack1llll111_opy_:
    hostname = bstack1lll1l_opy_(url)
    is_private = bstack11111lll_opy_(hostname)
    if (bstack111lll1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫຨ") in CONFIG and not CONFIG[bstack111lll1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬຩ")]) and (is_private or bstack11ll11l_opy_):
      bstack1llll111_opy_ = hostname
def bstack1lll1l_opy_(url):
  return urlparse(url).hostname
def bstack11111lll_opy_(hostname):
  for bstack1ll1l1l_opy_ in bstack1llll11l1_opy_:
    regex = re.compile(bstack1ll1l1l_opy_)
    if regex.match(hostname):
      return True
  return False