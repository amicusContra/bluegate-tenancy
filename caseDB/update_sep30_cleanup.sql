-- Cleanup: mark Sep 29 hearing as completed (denied)
UPDATE hearings SET status = 'completed', outcome = 'All 3 DaSean PPOs denied. Kevin admonished for UPL. AOP discovered post-hearing.' WHERE id = 'ppo-hearing-sep29';

-- Remove duplicate triplett-oct9 (same as cmc-oct9)
DELETE FROM hearings WHERE id = 'triplett-oct9';
