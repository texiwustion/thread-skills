#!/usr/bin/env python3
"""Initialize the thread-system template layout inside a repository root."""

from __future__ import annotations

import argparse
from pathlib import Path


MEMORY_TEMPLATE = """# Thread Memory

## Identity
- Thread: <thread-id>
- Status: active
- Goal: <中文，一句话目标>

## SuccessCriteria
- [sc-001] <中文，可验证成功标准>

## Constraints
- [constraint-001] <中文，线程边界/限制>

## ConfirmedFacts
- [fact-001] <中文，已确认事实> | Source: <路径/测试/提交/观察>

## Decisions
- [decision-001] <中文，已定决策> | Reason: <中文，为什么这样定>

## OpenQuestions
- [question-001] <中文，未决问题>

## CurrentState
- <中文，当前线程所处状态，2-5 条即可>

## NextStepContract
- ContractId: nsc-001
- Status: active
- Objective: <中文，本轮唯一目标>

### Allowed
- 可读取的范围：
  - ...
- 可修改的目标：
  - ...
- 可执行的动作：
  - ...
- 可产出的结果：
  - ...

### Disallowed
- 不允许修改：
  - ...
- 不允许顺手处理：
  - ...
- 不允许新增：
  - ...
- 不允许做的判断：
  - ...

### Deliverable
- 本轮完成后必须看到：
  - ...

### Verification
- Must pass:
  - ...
- Must inspect:
  - ...
- Failure policy:
  - 任一必过项失败则本轮停止，不得提代码 PR

### StopConditions
- ...

### ScopeLimit
- 最大允许改动文件数：...
- 最大允许改动模块数：...
- 是否允许跨目录：yes|no
- 是否允许改接口/数据结构：yes|no

### EscalateWhen
- ...

## References
- ...
"""

INTERRUPT_TEMPLATE = """# Interrupt Record

## RunMeta
- RunId: <rYYYYMMDD-NN>
- Thread: <thread-id>
- Actor: codex|interactive-codex|human
- StartTime: <ISO8601>
- EndTime: <ISO8601>
- RepoHeadStart: <git sha>
- ThreadMemoryRevision: <git sha|draft>
- PlatformMemorySource: <repo/path>
- PlatformMemoryVersion: <git sha|pending>
- PlatformMemoryFilesUsed:
  - <path>|none
- ScopeRespected: yes|no

## RunIntent
- <中文，本轮打算做什么>

## InputSnapshot
- 本轮使用的线程记忆摘要：
  - ...
- 本轮使用的合同摘要：
  - ...

## ActionsTaken
- ...

## ArtifactsProduced
- 代码改动：
  - ...
- 文档改动：
  - ...
- 提案文件：
  - none | memory-proposal.md | platform-memory-proposal.md

## VerificationResult
- Passed:
  - ...
- Failed:
  - ...
- NotRun:
  - ...

## Outcome
- Status: advanced|blocked|done|noop

## StoppedBecause
- <中文，必须具体>

## NextStep
- <中文，下一步建议，仅一条主建议>

## EscalateToHuman
- <中文，需要你确认的点；没有则写 none>
"""

MEMORY_PROPOSAL_TEMPLATE = """# Memory Proposal

## ProposalMeta
- Thread: <thread-id>
- ProducedByRunId: <run-id>
- BasedOnThreadMemoryRevision: <git sha>
- BasedOnPlatformMemoryVersion: <git sha>

## ProposedFacts
- Target: ConfirmedFacts
- Change: add|deprecate
- Content: <中文>
- Evidence: <路径/测试/提交/观察>

## ProposedDecisionUpdates
- Target: Decisions
- Change: add|supersede
- Content: <中文>
- Reason: <中文>

## ProposedStateUpdate
- Target: CurrentState|OpenQuestions|NextStepContract
- Change: <中文>
- Reason: <中文>
- Evidence: <中文或引用>

## ReviewerChecklist
- [ ] 证据足够
- [ ] 未越过线程边界
- [ ] 未把假设写成事实
- [ ] 未把局部经验升级为平台规律
"""

PLATFORM_MEMORY_PROPOSAL_TEMPLATE = """# Platform Memory Proposal

## ProposalMeta
- SourceThread: <thread-id>
- ProducedByRunId: <run-id>
- TargetPlatformMemory: <platform>.md
- BasedOnPlatformMemoryVersion: <git sha>

## ProposedPlatformFacts
- Change: add|deprecate
- Content: <中文>
- Evidence: <路径/测试/提交/观察>

## ProposedPlatformDecisionUpdates
- Change: add|supersede
- Content: <中文>
- Reason: <中文>

## ReviewerChecklist
- [ ] 证据足够
- [ ] 已跨线程验证
- [ ] 不是单线程局部经验
- [ ] 适合升级为平台规律
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root where the thread system should be initialized.",
    )
    return parser.parse_args()


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def init_thread_repo(repo_root: Path) -> Path:
    template_dir = repo_root / "threads" / "_template"
    template_dir.mkdir(parents=True, exist_ok=True)

    write_if_missing(template_dir / "memory.md", MEMORY_TEMPLATE)
    write_if_missing(template_dir / "interrupt.md", INTERRUPT_TEMPLATE)
    write_if_missing(template_dir / "memory-proposal.md", MEMORY_PROPOSAL_TEMPLATE)
    write_if_missing(template_dir / "platform-memory-proposal.md", PLATFORM_MEMORY_PROPOSAL_TEMPLATE)

    return template_dir


def main() -> int:
    args = parse_args()
    init_thread_repo(Path(args.repo_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
