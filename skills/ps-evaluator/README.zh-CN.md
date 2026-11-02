# PS Evaluator Skill v0.2.0

本科个人陈述评估 Skill，采用**动态专业研究**模式，适用于港五及其他大学。Skill 内不预置 HKU、HKUST 等特定 Major 的固定画像，也不会杜撰各校内部 PS 评分权重。

## 工作流程

1. 确认大学、准确专业名称、入学年份、申请途径，以及同一篇 PS 是否覆盖多个志愿。
2. 使用可用的搜索能力查找官方英文招生要求和专业培养目标。分别记录提交规则、课程事实、推导出的专业相关能力、未解决事项及资料来源。
3. 先用统一 Rubric 评价文章本身的质量（70 分），再针对**每个目标专业**单独评价匹配度（30 分）。70/30 是研究用途的实验权重，不代表港校官方标准。
4. 输出原文证据、评分理由、重要问题、各专业匹配度、可靠性提示及来源。若无法核实官方专业资料，只输出通用评估或注明专业评分暂不可靠。
5. 支持不同版本比较、同一文书跨专业比较和 Benchmark 一致性测试。

## 安装

```bash
npx skills add who-andy/AIOS-in-Project-Memory --skill ps-evaluator
```

也可以将 `skills/ps-evaluator/` 放到 Claude Code 的 `~/.claude/skills/ps-evaluator/` 或 Codex 的 `~/.agents/skills/ps-evaluator/`。Skill 不依赖 AIOS，不需要默认购买模型 API。

## 调用例子

> 使用 ps-evaluator 评估我的 2027 年国际 A-Level 申请 PS，目标为[大学][完整专业名]。先核对官方英文招生规定和课程结构，给出出处，再评价文章质量和专业匹配度。如果同一篇 PS 覆盖两个志愿，分别检查两者。

## 结构检查

```bash
cd skills/ps-evaluator
python3 scripts/validate_profiles.py --root .
python3 -m unittest discover -s tests -v
python3 scripts/aggregate_scores.py --rubrics . --input examples/evaluations.synthetic.json
python3 scripts/benchmark.py --input examples/benchmark.synthetic.json
```

Python 脚本验证评分格式、求和和评委分歧，不负责上网、调用 AI 或验证录取概率。示例样本均为虚构数据。详细规则见 `references/research-protocol.md` 和 `references/output-schema.md`。

真实 PS、申请人资料、个人化评估报告不得擅自提交到公共 GitHub。
