import time
from src.tasks.BaseEfTask import BaseEfTask


class Test(BaseEfTask):
    """
    简单箭头角度读取测试
    直接调用 get_arrow_angle() 并持续输出当前角度
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "箭头角度实时读取"
        self.description = "持续读取并显示当前箭头的角度"

        self.interval = 0.3  # 读取间隔（秒）

    def run(self):
        self.log_info("=== 箭头角度实时检测开始 ===", notify=True)
        self.log_info("按 Ctrl+C 停止\n")

        try:
            iteration = 0
            while True:
                iteration += 1

                # 直接调用 API 获取角度
                angle, score = self.get_arrow_angle(
                    two_stage=True,  # 推荐开启两阶段搜索
                    benchmark_width=2560,
                )

                status = "✓" if score > 0.75 else "⚠"

                self.log_info(f"{status} [#{iteration:03d}] " f"角度: {angle:6.1f}°    " f"置信度: {score:.4f}")

                # 每 10 次输出一次分隔线
                if iteration % 10 == 0:
                    self.log_info("-" * 50)

                time.sleep(self.interval)

        except KeyboardInterrupt:
            self.log_info("\n已停止角度检测", notify=True)
        except Exception as e:
            self.log_info(f"发生错误: {e}", notify=True)
