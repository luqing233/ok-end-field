from qfluentwidgets import FluentIcon

from src.tasks.daily.daily_battle_mixin import DailyBattleMixin


class BattleTask(DailyBattleMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "刷体力"
        self.description = "使用说明参见选项，更多用法参见 ./docs/体力本.md"
        self.icon = FluentIcon.BRIGHTNESS
        self.default_config_group.pop("⭐刷体力", None)
        self.default_config.pop("⭐刷体力", None)

    def run(self):
        self.ensure_main(time_out=420)
        try:
            ok = self.battle()
            if ok:
                self.log_info("刷体力结束!", notify=self.config.get("后台结束战斗通知") and self.in_bg())
            else:
                self.log_info("未检测到刷体力正常结束,可能未进入战斗或战斗异常,请检查")
        finally:
            # 显式释放 YOLO/OpenVINO 相关资源，避免长期驻留在进程内存中。
            self.release_yolo_detector()
