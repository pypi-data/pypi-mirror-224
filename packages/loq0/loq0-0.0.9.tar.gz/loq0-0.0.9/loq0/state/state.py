import numpy as np
from ..const import BOARD_SIZE, I_COUNT, L_COUNT


class State:
    def __init__(self, state=None, dtype=np.uint8):
        if state is None:
            self.st = np.zeros((2 + (I_COUNT + L_COUNT) * 2, 3), dtype=dtype)
            self.st[0, 0] = (BOARD_SIZE + 1) // 2
            self.st[0, 1] = 1
            self.st[1, 0] = (BOARD_SIZE + 1) // 2
            self.st[1, 1] = BOARD_SIZE
        else:
            self.st = state

    def copy(self):
        return State(self.st.copy())

    def player(self, op=None):
        if op is None:
            return self.st[0, 2]
        return 1 - self.st[0, 2]

    def internal(self, op=None):
        pl = self.player(op)
        return 4 <= self.st[pl, 0] <= 6 and 4 <= self.st[pl, 1] <= 6

    def i_walls(self):
        return self.st[2 + np.array(*np.where(self.st[2:2 + I_COUNT * 2, 0] != 0)), :]

    def l_walls(self):
        return self.st[2 + I_COUNT * 2 + np.array(*np.where(self.st[2 + I_COUNT * 2:, 0] != 0)), :]

    def position(self, op=None):
        pl = self.player(op)
        return self.st[pl, 0], self.st[pl, 1]

    def win(self):
        if self.st[0, 1] == BOARD_SIZE:
            return 0
        elif self.st[1, 1] == 1:
            return 1
        return None

    def blind(self):
        st = self.copy()
        if st.internal(True):
            pl = st.player(True)
            st.st[pl, 0] = st.st[pl, 1] = -1
        if not st.internal():
            for i in range(2, 2 + I_COUNT * 2):
                if st.st[i, 2] == 1:
                    if 4 < st.st[i, 0] < 7 and 3 < st.st[i, 1] < 6:
                        st.st[i, 0] = st.st[i, 1] = st.st[i, 2] = -1
                if st.st[i, 2] == 2:
                    if 4 < st.st[i, 1] < 7 and 3 < st.st[i, 0] < 6:
                        st.st[i, 0] = st.st[i, 1] = st.st[i, 2] = -1
            for i in range(2 + I_COUNT * 2, 2 + (I_COUNT + L_COUNT) * 2):
                if st.st[i, 2] == 1:
                    if 3 < st.st[i, 0] < 7 and 3 < st.st[i, 1] < 7 and not (st.st[i, 0] == 4 and st.st[i, 1] == 4):
                        st.st[i, 0] = st.st[i, 1] = st.st[i, 2] = -1
                if st.st[i, 2] == 2:
                    if 3 < st.st[i, 0] < 7 and 3 < st.st[i, 1] < 7 and not (st.st[i, 0] == 4 and st.st[i, 1] == 6):
                        st.st[i, 0] = st.st[i, 1] = st.st[i, 2] = -1
                if st.st[i, 2] == 3:
                    if 3 < st.st[i, 0] < 7 and 3 < st.st[i, 1] < 7 and not (st.st[i, 0] == 6 and st.st[i, 1] == 6):
                        st.st[i, 0] = st.st[i, 1] = st.st[i, 2] = -1
                if st.st[i, 2] == 4:
                    if 3 < st.st[i, 0] < 7 and 3 < st.st[i, 1] < 7 and not (st.st[i, 0] == 6 and st.st[i, 1] == 4):
                        st.st[i, 0] = st.st[i, 1] = st.st[i, 2] = -1
        return st

    def blocks(self):
        h_blocks = np.zeros(size=(BOARD_SIZE + 1, BOARD_SIZE - 1), dtype=np.bool)
        v_blocks = np.zeros(size=(BOARD_SIZE - 1, BOARD_SIZE + 1), dtype=np.bool)
        for i in range(2, 2 + I_COUNT * 2):
            if self.st[i, 2] == 1:
                h_blocks[self.st[i, 0], self.st[i, 1]] = True
                h_blocks[self.st[i, 0], self.st[i, 1] + 1] = True
            elif self.st[i, 2] == 2:
                v_blocks[self.st[i, 0], self.st[i, 1]] = True
                v_blocks[self.st[i, 0] + 1, self.st[i, 1]] = True
        for i in range(2 + I_COUNT * 2, 2 + (I_COUNT + L_COUNT) * 2):
            if self.st[i, 2] == 1:
                h_blocks[self.st[i, 0], self.st[i, 1]] = True
                v_blocks[self.st[i, 0], self.st[i, 1]] = True
            elif self.st[i, 2] == 2:
                h_blocks[self.st[i, 0], self.st[i, 1]] = True
                v_blocks[self.st[i, 0], self.st[i, 1] + 1] = True
            elif self.st[i, 2] == 3:
                h_blocks[self.st[i, 0] + 1, self.st[i, 1]] = True
                v_blocks[self.st[i, 0], self.st[i, 1] + 1] = True
            elif self.st[i, 2] == 4:
                h_blocks[self.st[i, 0] + 1, self.st[i, 1]] = True
                v_blocks[self.st[i, 0], self.st[i, 1]] = True
        return h_blocks, v_blocks

    from .validate.blocked import horizontal_block, vertical_block
    from .validate.movable import movable
    from .validate.endable import endable
    from .validate.cross import cross
    from .validate.internal import block_internal

    from .actions import move, place_i, place_l
    from .actions import act
    from .print import __str__
